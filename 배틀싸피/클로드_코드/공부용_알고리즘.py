# =====================================================================
#  배틀싸피 탱크 알고리즘 — 공부용 (알고리즘 부분만)
# =====================================================================
#
#  [이 파일에 없는 것 = 시험장 기본 코드에 이미 있는 것 → 외울 필요 X]
#    - 통신            : init, submit, close
#    - 데이터 읽기     : parse_data  (map_data 등에 저장해 줌)
#    - 위치 찾기       : find_positions(grid, 'M', 'X')  →  (내 위치, 포탑 위치)
#    - 방향 설정       : DIRS, MOVE_CMDS, FIRE_CMDS
#        DIRS      = [(0, 1), (1, 0), (0, -1), (-1, 0)]      # 0=오른쪽 1=아래 2=왼쪽 3=위
#        MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
#        FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
#      ⚠️ 이 세 줄은 기본 코드의 "알고리즘 함수 구현" 구간 안에 있으니 지우지 말 것!
#
#  [외우는 순서]  ⭐ 많을수록 먼저
#    ⭐⭐⭐ [1] trees_in_line : 여기서 쏘면 포탑에 맞나? (사거리 3칸)
#    ⭐⭐⭐ [2] search        : 기본 bfs를 고친 최단 경로  (★ = 기본 bfs와 다른 줄)
#    ⭐⭐⭐ [6] decide        : 매 턴 무엇을 할지 정하는 두뇌
#    ⭐⭐   [3] 포탄 계산      : count_trees, enough_ammo, first_command
#    ⭐⭐   [5] decode        : 카이사르 암호 풀기
#    ⭐     [4] supply_path   : 어느 보급시설 옆 칸으로 갈지
#    ⭐     메인 부분의 "암호 실패 처리" (간격이 틀렸을 때를 위한 보험)
#
#  [전체 흐름 한 줄 요약]
#    매 턴: 쏠 자리까지 최단 경로 찾기 → 포탄 충분? → 예: 첫 명령 실행
#                                                  → 아니오: 보급시설 가서 암호 해독
# =====================================================================

import heapq        # 기본 코드에는 deque만 있으니 이 줄은 추가해야 해

# 내가 정하는 설정값
ROAD = ['G', 'S', 'M']             # 탱크가 지나갈 수 있는 칸 (M = 내 자리, 움직이면 빈 땅)
SHELL_PASS = ['G', 'S', 'W', 'M']  # 포탄이 그냥 통과하는 칸 (물 위로는 포탄이 날아감)

SHIFT = 17             # 카이사르 암호 간격 (매뉴얼 예시: SRKKCVJJRWP → BATTLESSAFY)
tried_decode = False   # 지난 턴에 암호 해독을 시도했는지 (보험용)
mega_before = 0        # 해독 시도 직전의 메가 포탄 수 (보험용)


# ---------------------------------------------------------------
# [1] 여기서 d 방향으로 쏘면 포탑에 맞나?   ⭐⭐⭐
# ---------------------------------------------------------------
def trees_in_line(grid, r, c, d):
    """포탑까지 사이에 있는 나무 수를 돌려준다.
       0 = 바로 맞힐 수 있음 / 1 이상 = 나무를 먼저 치워야 함 / -1 = 못 맞힘"""
    dr, dc = DIRS[d] #DIRS      = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    trees = 0
    for k in range(1, 4):                        # 1칸, 2칸, 3칸 앞을 차례로 확인
        nr, nc = r + dr * k, c + dc * k
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
            return -1                            # 맵 밖
        if grid[nr][nc] == 'X':
            return trees                         # 포탑 발견! "오는 길에 나무를 몇 개 지나쳤는지"(trees)를 돌려주는 거지. 나무를 하나도 안 지나쳤으면 trees가 그대로 0이니까 0이 나와. # trees가 1이면 포탄을 2개 쏴야 포탑을 맞춤
        if grid[nr][nc] == 'T':
            trees += 1                           # 나무는 쏴서 치울 수 있음
        elif grid[nr][nc] not in SHELL_PASS:
            return -1                            # 바위, 보급시설에 막힘
    return -1                                    # 3칸 안에 포탑이 없음


# ---------------------------------------------------------------
# [2] 최단 경로 찾기 (기본 bfs를 고친 것)   ⭐⭐⭐
# ---------------------------------------------------------------
#  기본 bfs에서 바뀐 점 (★ 표시한 줄)
#   ★1 deque → heapq   : 나무 칸은 2턴(쏘기+이동)이라 "명령 수가 적은 것부터" 꺼내야 함
#   ★2 != wall → ROAD  : 바위뿐 아니라 물, 보급시설도 못 지나가게
#   ★3 바로 옆만 → 3칸 : 3칸 거리에서도 쏠 수 있으면 거기서 쏨 (턴 절약)
#   ★4 나무 칸         : "쏘고 + 이동" 명령 2개로 지나감 (max_trees 개까지만)
#   ★5 visited         : 부순 나무 수도 같이 기록
def search(grid, start, goal, max_trees):
    """start에서 goal까지 가는 명령 목록 (명령 수가 가장 적은 것)
       goal = 'X'     : 포탑을 쏠 수 있는 자리까지 가서 발사
       goal = (행, 열) : 그 칸까지 이동"""
    queue = [(0, start, 0, [])]          # ★1 (명령 수, 위치, 부순 나무 수, 명령 목록)
    visited = set()

    while queue:
        count, (r, c), trees, actions = heapq.heappop(queue)    # ★1 명령 수가 가장 적은 것부터
        if len(actions) > 0 and actions[-1].endswith('F'):
            return actions               # ★3 발사로 끝나는 계획 = 포탑 공격까지 완성!
        if (r, c, trees) in visited:     # ★5
            continue
        visited.add((r, c, trees))       # ★5

        if (r, c) == goal:               # 목표 칸에 도착
            return actions

        # ★3 여기서 포탑을 쏠 수 있으면 '완성된 계획'을 줄에 넣어 둔다
        if goal == 'X':
            for d in range(4):
                line = trees_in_line(grid, r, c, d)
                if line >= 0 and trees + line <= max_trees:
                    # 사이의 나무 수만큼 먼저 쏘기
                    plan = actions + [FIRE_CMDS[d]] * (line + 1)    # FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
                    heapq.heappush(queue, (len(plan), (r, c), trees + line, plan))

        # 상하좌우 이웃 칸으로 가 보기
        for d in range(4):
            nr, nc = r + DIRS[d][0], c + DIRS[d][1] #DIRS      = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue
            if grid[nr][nc] in ROAD:                                 # ★2 빈 땅: 이동(1턴)
                new_actions = actions + [MOVE_CMDS[d]] # MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
                new_trees = trees
            elif grid[nr][nc] == 'T' and trees < max_trees:          # ★4 나무: 쏘고+이동(2턴)
                new_actions = actions + [FIRE_CMDS[d], MOVE_CMDS[d]]
                new_trees = trees + 1
            else:                                                    # 물, 바위, 보급시설
                continue
            heapq.heappush(queue, (len(new_actions), (nr, nc), new_trees, new_actions))

    return None                          # 갈 수 있는 길이 없음


# ---------------------------------------------------------------
# [3] 포탄 계산   ⭐⭐
# ---------------------------------------------------------------
def count_trees(path):
    """길 중간의 발사 명령 수 = 부술 나무 수 (마지막 발사는 포탑용이라 뺌)"""
    trees = 0
    for cmd in path[:-1]:
        if cmd.endswith('F'):
            trees += 1
    return trees


def enough_ammo(path, normal, mega, x_hp):
    """이 길로 가서 나무까지 부순 뒤에도 포탑을 부술 포탄이 남는가?"""
    for i in range(count_trees(path)):   # 나무에는 일반 포탄부터 쓰기
        if normal > 0:
            normal -= 1
        elif mega > 0:
            mega -= 1
        else:
            return False
    return normal * 30 + mega * 70 >= x_hp      # 일반 30, 메가 70 데미지


def first_command(path, normal, mega, x_hp):
    """길의 첫 명령. 발사라면 일반/메가 중 뭘 쏠지 정해서 ' M'을 붙인다."""
    cmd = path[0]
    if cmd.endswith('F'):
        if len(path) == 1:      # 마지막 명령 = 포탑 공격 → 메가 우선
            use_mega = mega > 0 and (x_hp > 30 or normal == 0)
        else:                   # 나무 공격 → 일반 우선 (메가는 포탑용으로 아낌)
            use_mega = (normal == 0)
        if use_mega:
            cmd = cmd + ' M'
    return cmd


# ---------------------------------------------------------------
# [4] 보급시설로 가는 길   ⭐
# ---------------------------------------------------------------
def supply_path(grid, me, shells):
    """보급시설 옆 칸 중 '나 → 그 칸 → 포탑' 이 가장 짧은 칸으로 가는 길"""
    best, best_total = None, None
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != 'F':
                continue
            for dr, dc in DIRS:                            # 보급시설의 상하좌우 칸
                q = (r + dr, c + dc)
                if not (0 <= q[0] < len(grid) and 0 <= q[1] < len(grid[0])):
                    continue
                if grid[q[0]][q[1]] not in ROAD + ['T']:
                    continue
                path1 = search(grid, me, q, shells)        # 나 → 보급시설 옆 칸
                path2 = search(grid, q, 'X', 10)           # 보급시설 옆 칸 → 포탑
                if path1 is None or path2 is None:
                    continue
                total = len(path1) + len(path2)
                if best_total is None or total < best_total:
                    best, best_total = path1, total
    return best


# ---------------------------------------------------------------
# [5] 카이사르 암호 풀기   ⭐⭐
# ---------------------------------------------------------------
def decode(code):
    """알파벳을 SHIFT칸씩 앞으로 되돌린다. 예) SHIFT=17 이면 S → B"""
    answer = ''
    for ch in code:
        num = ord(ch) - ord('A')        # A=0, B=1, ..., Z=25
        num = (num - SHIFT) % 26        # 되돌리기 (A보다 앞이면 Z로 넘어감)
        answer += chr(num + ord('A'))
    return answer


# ---------------------------------------------------------------
# [6] 이번 턴에 할 행동 정하기 (두뇌)   ⭐⭐⭐
# ---------------------------------------------------------------
def decide(grid, normal, mega, x_hp, codes):
    me, target = find_positions(grid, 'M', 'X')     # 기본 코드 함수 사용

    # (1) 나무를 0개, 1개, 2개 ... 부수는 길을 차례로 구해 보고,
    #     포탄이 충분한 길 중 가장 짧은 길을 고른다
    best = None
    for max_trees in range(normal + mega + 1):
        path = search(grid, me, 'X', max_trees)
        if path is not None and enough_ammo(path, normal, mega, x_hp):
            if best is None or len(path) < len(best):
                best = path
    if best is not None:
        return first_command(best, normal, mega, x_hp)

    # (2) 포탄 부족 → 보급시설 옆이면 암호 해독, 아니면 보급시설로 이동
    if len(codes) > 0:
        return 'G ' + decode(codes[0])
    path = supply_path(grid, me, normal + mega)
    if path:
        return first_command(path, normal, mega, x_hp)

    # (3) 할 수 있는 게 없으면 대기
    return 'S'


# =====================================================================
#  ↓↓↓ 여기부터는 while 반복문 안 ("알고리즘 메인 부분 구현 시작 ~ 끝") ↓↓↓
# =====================================================================
while game_data is not None:

    # (1) 기본 코드의 parse_data로 이번 턴 데이터 읽기
    parse_data(game_data)

    # (2) 필요한 정보 꺼내기
    #   ⚠️ 시험장에서 꼭 확인할 부분! (이 파일에서 유일하게 기본 코드에 맞춰야 하는 곳)
    #      parse_data 안에서 "M 100 R 1 0" 줄과 "X 10" 줄, 암호문이 어떤 변수에
    #      저장되는지 보고 아래 이름을 맞춰 줘. 아래는 흔한 형태로 짐작한 예시야.
    #        M 100 R 1 0  →  my_allies['M'] = ['100', 'R', '1', '0']
    #        X 10         →  enemies['X']   = ['10']
    grid = map_data
    normal = int(my_allies['M'][2])      # 일반 포탄 수
    mega = int(my_allies['M'][3])        # 메가 포탄 수
    x_hp = int(enemies['X'][0])          # 포탑 체력
    # 암호문 목록은 codes 라는 리스트에 있다고 가정 (예: ['AKWNSDN'])

    # (3) [보험] 지난 턴에 암호를 풀었는데 메가 포탄이 안 늘었으면 → 간격을 하나 바꿔 보기
    if tried_decode:
        if mega > mega_before:
            print('[암호] 해독 성공! 간격 =', SHIFT)
        else:
            SHIFT = (SHIFT + 1) % 26
            print('[암호] 해독 실패... 다음엔 간격', SHIFT)
    tried_decode = False

    # (4) 명령 정하기 (오류가 나도 프로그램이 죽지 않게 try로 감싸기)
    try:
        output = decide(grid, normal, mega, x_hp, codes)
    except Exception as e:
        print('[오류]', e)
        output = 'S'

    if output.startswith('G'):           # 암호 해독 턴이면 기록 (보험용)
        tried_decode = True
        mega_before = mega

    print(f'[내 탱크] 일반 {normal}, 메가 {mega}, 포탑 체력 {x_hp} → 명령: {output}')

    # (5) 명령 보내고 다음 턴 데이터 받기
    game_data = submit(output)
