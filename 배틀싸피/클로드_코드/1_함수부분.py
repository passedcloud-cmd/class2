##############################
# 알고리즘 함수/메서드 부분 구현 시작
##############################
# [붙여넣는 곳]
#   main.py 의 "알고리즘 함수/메서드 부분 구현 시작" ~ "끝" 사이에 있던 코드를
#   전부 지우고, 이 파일 내용을 통째로 붙여넣기
import heapq

# ---------------------------------------------------------------
# 기본 설정
# ---------------------------------------------------------------
# 방향 번호: 0=오른쪽, 1=아래, 2=왼쪽, 3=위  (기본 코드와 같은 순서)
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
MOVE_CMDS = {0: 'R A', 1: 'D A', 2: 'L A', 3: 'U A'}   # 그 방향으로 한 칸 이동
FIRE_CMDS = {0: 'R F', 1: 'D F', 2: 'L F', 3: 'U F'}   # 그 방향으로 발사

# M(내 탱크 자리)도 넣어 둔 이유: 내가 움직이고 나면 그 칸은 빈 땅이 되니까
ROAD = ['G', 'S', 'M']             # 탱크가 지나갈 수 있는 칸 (풀, 모래)
SHELL_PASS = ['G', 'S', 'W', 'M']  # 포탄이 그냥 통과하는 칸 (풀, 모래, 물)

SHIFT = 17             # 카이사르 암호 간격 (매뉴얼 예시 SRKKCVJJRWP → BATTLESSAFY 에서 찾음)
tried_decode = False   # 지난 턴에 암호 해독을 시도했는지
mega_before = 0        # 해독을 시도하기 직전의 메가 포탄 수


# ---------------------------------------------------------------
# 1. 서버가 보낸 데이터 읽기
# ---------------------------------------------------------------
def read_game(game_data):
    """서버가 보낸 글자 데이터에서 필요한 정보만 꺼낸다."""
    lines = game_data.strip().split('\n')
    first = lines[0].split()
    height = int(first[0])                       # 맵 세로 크기
    unit_count = int(first[2]) + int(first[3])   # 아군 수 + 적군 수

    grid = []                                    # 맵. grid[행][열] 로 사용
    for i in range(1, height + 1):
        grid.append(lines[i].split())

    normal, mega, x_hp = 0, 0, 0
    unit_lines = lines[height + 1:]              # 맵 아래쪽 줄들
    for line in unit_lines[:unit_count]:
        parts = line.split()
        if parts[0] == 'M':                      # 예) M 100 R 1 0
            normal = int(parts[3])               #     → 일반 포탄 1개
            mega = int(parts[4])                 #     → 메가 포탄 0개
        elif parts[0] == 'X':                    # 예) X 10
            x_hp = int(parts[1])                 #     → 포탑 체력 10

    codes = []                                   # 나머지 줄 = 암호문
    for line in unit_lines[unit_count:]:
        if line.strip() != '':
            codes.append(line.strip())

    return grid, normal, mega, x_hp, codes


# ---------------------------------------------------------------
# 2. 작은 도우미 함수들
# ---------------------------------------------------------------
def find(grid, symbol):
    """맵에서 symbol 글자가 있는 위치 (행, 열) 찾기"""
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == symbol:
                return (r, c)
    return None


def inside(grid, r, c):
    """(r, c)가 맵 안쪽인지 확인"""
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def trees_in_line(grid, r, c, d):
    """(r, c)에서 d 방향으로 쏠 때, 포탑(X) 사이에 있는 나무 수 (사거리 3칸)
       0 이면 바로 맞힐 수 있음, -1 이면 포탑을 맞힐 수 없음"""
    dr, dc = DIRS[d]
    trees = 0
    for k in range(1, 4):                        # 1칸, 2칸, 3칸 앞을 차례로 확인
        nr, nc = r + dr * k, c + dc * k
        if not inside(grid, nr, nc):
            return -1
        if grid[nr][nc] == 'X':
            return trees
        if grid[nr][nc] == 'T':                  # 나무는 쏴서 치울 수 있음
            trees += 1
        elif grid[nr][nc] not in SHELL_PASS:     # 바위, 보급시설 등에 막힘
            return -1
    return -1                                    # 3칸 안에 포탑이 없음


def count_trees(path):
    """길 중간에 나오는 발사 명령 수 = 부숴야 하는 나무 수 (마지막 발사는 포탑용)"""
    trees = 0
    for cmd in path[:-1]:
        if cmd.endswith('F'):
            trees += 1
    return trees


# ---------------------------------------------------------------
# 3. 최단 경로 찾기 (기본 코드의 bfs를 조금 고친 것)
# ---------------------------------------------------------------
def search(grid, start, goal, max_trees):
    """start에서 goal까지 가는 '명령 개수가 가장 적은' 명령 목록을 찾는다.
       goal = 'X'      : 포탑을 쏠 수 있는 자리까지 가서 발사
       goal = (행, 열)  : 그 칸까지 이동
       max_trees       : 길을 막은 나무를 최대 몇 개까지 부수고 지나갈지"""
    queue = [(0, start, 0, [])]       # (명령 개수, 위치, 부순 나무 수, 명령 목록)
    visited = set()

    while queue:
        count, (r, c), trees, actions = heapq.heappop(queue)   # 명령 개수가 가장 적은 것부터 꺼냄
        if len(actions) > 0 and actions[-1].endswith('F'):
            return actions            # 발사로 끝나는 계획 = 포탑 공격까지 완성된 계획
        if (r, c, trees) in visited:
            continue
        visited.add((r, c, trees))

        # 목표 칸에 도착했는지 확인
        if (r, c) == goal:
            return actions

        # 여기서 포탑을 쏠 수 있다면 '완성된 계획'을 줄에 넣어 둔다
        # (사이에 나무가 있으면 그 수만큼 먼저 쏴서 치움)
        if goal == 'X':
            for d in range(4):
                line = trees_in_line(grid, r, c, d)
                if line >= 0 and trees + line <= max_trees:
                    plan = actions + [FIRE_CMDS[d]] * (line + 1)
                    heapq.heappush(queue, (len(plan), (r, c), trees + line, plan))

        # 상하좌우 이웃 칸으로 가 보기
        for d in range(4):
            nr, nc = r + DIRS[d][0], c + DIRS[d][1]
            if not inside(grid, nr, nc):
                continue
            if grid[nr][nc] in ROAD:                          # 빈 땅: 이동 (1턴)
                new_actions = actions + [MOVE_CMDS[d]]
                new_trees = trees
            elif grid[nr][nc] == 'T' and trees < max_trees:   # 나무: 쏘고(1턴) + 이동(1턴)
                new_actions = actions + [FIRE_CMDS[d], MOVE_CMDS[d]]
                new_trees = trees + 1
            else:                                             # 물, 바위, 보급시설: 못 감
                continue
            heapq.heappush(queue, (len(new_actions), (nr, nc), new_trees, new_actions))

    return None                                               # 갈 수 있는 길이 없음


# ---------------------------------------------------------------
# 4. 포탄 계산
# ---------------------------------------------------------------
def enough_ammo(path, normal, mega, x_hp):
    """이 길대로 가면 (나무를 부수고 나서도) 포탑을 부술 포탄이 남는지 계산"""
    for i in range(count_trees(path)):   # 나무에는 일반 포탄부터 사용
        if normal > 0:
            normal -= 1
        elif mega > 0:
            mega -= 1
        else:
            return False                 # 나무 부술 포탄조차 없음
    return normal * 30 + mega * 70 >= x_hp   # 남은 포탄으로 포탑을 부술 수 있나?


def first_command(path, normal, mega, x_hp):
    """길의 첫 번째 명령을 꺼낸다. 발사라면 일반/메가 포탄 중 무엇을 쏠지 정한다."""
    cmd = path[0]
    if cmd.endswith('F'):
        if len(path) == 1:          # 마지막 명령 = 포탑 공격 → 메가 포탄 우선
            use_mega = mega > 0 and (x_hp > 30 or normal == 0)
        else:                       # 나무 공격 → 일반 포탄 우선 (메가는 포탑용으로 아낌)
            use_mega = (normal == 0)
        if use_mega:
            cmd = cmd + ' M'
    return cmd


# ---------------------------------------------------------------
# 5. 보급시설로 가는 길 고르기
# ---------------------------------------------------------------
def supply_path(grid, me, shells):
    """보급시설 옆 칸들 중에서 '나 → 보급시설 옆 칸 → 포탑' 거리가 가장 짧은 칸으로 가는 길"""
    best, best_total = None, None
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != 'F':
                continue
            for dr, dc in DIRS:                            # 보급시설의 상하좌우 칸
                q = (r + dr, c + dc)
                if not inside(grid, q[0], q[1]) or grid[q[0]][q[1]] not in ROAD + ['T']:
                    continue
                path1 = search(grid, me, q, shells)        # 나 → 보급시설 옆 칸 (가진 포탄만큼만 나무 부수기)
                path2 = search(grid, q, 'X', 10)           # 보급시설 옆 칸 → 포탑 (메가 포탄으로 나무 부수기)
                if path1 is None or path2 is None:
                    continue
                total = len(path1) + len(path2)
                if best_total is None or total < best_total:
                    best, best_total = path1, total
    return best


# ---------------------------------------------------------------
# 6. 카이사르 암호 풀기
# ---------------------------------------------------------------
def decode(code):
    """알파벳을 SHIFT칸씩 앞으로 되돌려서 원래 문장을 구한다."""
    answer = ''
    for ch in code:
        num = ord(ch) - ord('A')    # A=0, B=1, ..., Z=25
        num = (num - SHIFT) % 26    # SHIFT칸 되돌리기 (A보다 앞이면 Z로 넘어감)
        answer += chr(num + ord('A'))
    return answer


# ---------------------------------------------------------------
# 7. 이번 턴에 할 행동 정하기
# ---------------------------------------------------------------
def decide(grid, normal, mega, x_hp, codes):
    """이번 턴에 보낼 명령 하나를 정한다."""
    me = find(grid, 'M')

    # (1) 나무를 0개, 1개, 2개 ... 부수는 길을 차례로 구해 보고,
    #     포탄이 충분한 길 중에서 가장 짧은 길을 고른다
    best = None
    for max_trees in range(normal + mega + 1):
        path = search(grid, me, 'X', max_trees)
        if path is not None and enough_ammo(path, normal, mega, x_hp):
            if best is None or len(path) < len(best):
                best = path
    if best is not None:
        return first_command(best, normal, mega, x_hp)

    # (2) 포탄이 부족하다 → 보급시설에서 메가 포탄을 얻는다
    if len(codes) > 0:                           # 보급시설 바로 옆이면 암호 해독
        return 'G ' + decode(codes[0])
    path = supply_path(grid, me, normal + mega)
    if path:                                     # 아니면 보급시설 쪽으로 이동
        return first_command(path, normal, mega, x_hp)

    # (3) 할 수 있는 게 없으면 제자리 대기
    return 'S'

##############################
# 알고리즘 함수/메서드 부분 구현 끝
##############################
