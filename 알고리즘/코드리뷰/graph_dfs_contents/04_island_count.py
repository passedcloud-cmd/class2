# 4단계: 섬 개수 세기 (연결 요소 찾기) - DFS 풀이 / BFS 풀이
#
# 2차원 격자 자체가 하나의 거대한 그래프입니다. 각 칸이 정점이고,
# 인접한 칸으로 이동할 수 있다는 규칙이 보이지 않는 간선입니다. (암시적 그래프)
#
# 학습 목표
#   - 격자 문제를 그래프 문제로 바꿔 볼 수 있다.
#   - 바깥 이중 for 루프와 탐색 함수의 역할을 각각 설명할 수 있다.
#   - 격자 DFS에서 재귀 깊이가 왜 문제가 되는지 실측으로 확인한다.
#
# 시간 복잡도: O(N * M)  - 모든 칸을 최대 한 번씩 방문
# 공간 복잡도: O(N * M)  - visited + (재귀 스택 또는 큐)

import sys
from collections import deque
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '04_input.txt')

# 격자 DFS는 재귀 깊이가 칸 수만큼 깊어집니다. 이 한 줄이 없으면 큰 입력에서 죽습니다.
# sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

# 이 문제는 대각선까지 포함한 8방향입니다.
# 대부분의 격자 문제는 상하좌우 4방향만 씁니다. 지문에서 '대각선' 을 먼저 찾는 습관을 들이세요.
#   4방향 -> 아래 배열의 앞 4개만 잘라 쓰면 됩니다.
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

print('=== 입력 격자 ===')
for row in grid:
    print(''.join('■' if cell else '·' for cell in row))
print()


# ------------------------------------------------------------
# [실습 1] DFS (재귀)
# ------------------------------------------------------------
def dfs(r, c, visited):
    # 1. 현재 칸을 방문 처리하세요.
    # TODO
    visited[r][c] = True 
    # 2. 8방향 이웃 (nr, nc) 를 확인하세요.
    #    - 먼저 격자 범위 안인지 확인합니다. 순서를 바꾸면 IndexError 가 납니다.
    #    - 그곳이 땅(1)이고 아직 방문 전이면 재귀 호출합니다.
    #
    # 조건을 if 두 개로 나눠도 되고, and 로 하나로 합쳐도 됩니다. 결과는 같습니다.
    # 합쳐도 안전한 이유는 파이썬의 and 가 왼쪽이 거짓이면 오른쪽을 아예 평가하지 않기
    # 때문입니다(단축 평가). 범위를 벗어난 인덱스로 grid 에 접근하는 일은 생기지 않습니다.
    for i in range(8):  # TODO
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위 확인을 먼저 해야 함
        if 0 <= nr < N and 0 <= nc < M:
            # 그 다음에 땅인지를 확인한다 + 방문한 적이 없는 땅이어야 함
            if grid[nr][nc] == 1 and not visited[nr][nc]:
                dfs(nr, nc, visited) # visited 누적해야 하니까 계속 들고 다님
                                


visited = [[False] * M for _ in range(N)]
island_count = 0

# [실습 2] 바깥 이중 루프
# 모든 칸을 훑되, 어떤 칸을 만났을 때만 '새 섬' 으로 세고 탐색을 시작해야 할까요?
"""
1.for 반복문 ==> 지도 전체를 탐색반
    = 거대한 지도를 왼쪽 위부터 오른쪽 아래까지 한칸 한칸 전부 다 스캔
    = 이 지도 탐색반의 목표는 ' 아직 우리가 가보지 않은 새로운 땅(1)'을 찾는 것
2. if 조건문 ==> 새로운 땅을 발견한 순간
    = 탐색반이 땅이면서, 방문한 적이 없는 곳을 찾았다면 새로운 섬을 발견했다고 카운팅 
3. dfs 함수 ==> 상륙 부대
    = 탐색반의 보고를 받은 상륙 부대는 해당 좌표에 상륙하여 dfs 탐색을 시작
    = 상륙 부대의 목표는 '섬 하나의 영역을 완전히 파악(방문처리)'
"""
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]: # TODO: 조건이 2개
            island_count += 1
            dfs(i, j, visited)

print(f'DFS 풀이 - 섬의 개수: {island_count}   <- 정답은 3 입니다')


# ------------------------------------------------------------
# [실습 3] BFS (큐)
# ------------------------------------------------------------
def bfs(start_r, start_c, visited):
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True

    while queue:
        r, c = queue.popleft()

        # 8방향 이웃을 확인하여, 땅이고 아직 방문 전이라면
        # 큐에 넣기 '직전에' 방문 처리를 하고 큐에 추가하세요.
        # 방문 처리를 뒤로 미루면 같은 칸이 큐에 여러 번 들어갑니다.
        # 조건 작성 방식은 실습 1과 같습니다.
        pass  # TODO


visited = [[False] * M for _ in range(N)]
island_count = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]:
            island_count += 1
            bfs(i, j, visited)

print(f'BFS 풀이 - 섬의 개수: {island_count}   <- 정답은 3 입니다')
print('=> 두 풀이의 결과는 같아야 합니다. 탐색 순서만 다를 뿐입니다.')
print()

# --- 동작 과정 시각화 (완성되어 있습니다) ---
# 섬마다 어떤 칸들이 한 덩어리로 묶이는지 확인합니다.
print('=== 섬별 구성 칸 ===')
visited = [[False] * M for _ in range(N)]
label = [[0] * M for _ in range(N)]
island_count = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]:
            island_count += 1
            cells = deque([(i, j)])
            visited[i][j] = True
            members = []

            while cells:
                r, c = cells.popleft()
                label[r][c] = island_count
                members.append((r, c))

                for k in range(8):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if grid[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            cells.append((nr, nc))

            print(f'{island_count}번 섬: 시작 {(i, j)} | 칸 {len(members)}개 {members}')

print()
print('섬 번호를 격자에 찍어 보면:')
for row in label:
    print(''.join(str(cell) if cell else '·' for cell in row))
print()

# --- 재귀 깊이 한계 확인 (완성되어 있습니다) ---
# 문제 제약은 1 <= N, M <= 100 입니다. 전부 땅이면 재귀 깊이가 10,000까지 갈 수 있습니다.
# 파이썬 기본 재귀 한계는 1000 이므로, 아무 조치 없이 재귀 DFS를 쓰면 죽습니다.
print('=== 재귀 깊이 한계 확인 ===')
print(f'현재 재귀 한계: {sys.getrecursionlimit()} (위에서 10**6 으로 올려둔 값)')


def probe(size, limit):
    """size x size 전부 땅인 격자를 재귀 DFS로 훑어본다."""
    old = sys.getrecursionlimit()
    sys.setrecursionlimit(limit)

    big_grid = [[1] * size for _ in range(size)]
    big_visited = [[False] * size for _ in range(size)]

    def walk(r, c):
        big_visited[r][c] = True
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < size and 0 <= nc < size:
                if big_grid[nr][nc] == 1 and not big_visited[nr][nc]:
                    walk(nr, nc)

    try:
        walk(0, 0)
        result = '정상 종료'
    except RecursionError:
        result = 'RecursionError'
    finally:
        sys.setrecursionlimit(old)

    return result


print(f'  기본 한계(1000) + 31x31 전부 땅 -> {probe(31, 1000)}')
print(f'  기본 한계(1000) + 32x32 전부 땅 -> {probe(32, 1000)}')
print(f'  한계 10**6     + 100x100 전부 땅 -> {probe(100, 10**6)}')
print()
print('문제 제약(N, M <= 100)의 1/10도 안 되는 32x32에서 이미 죽습니다.')
print('격자 DFS에서 sys.setrecursionlimit() 은 선택이 아니라 필수입니다.')
print('BFS는 재귀를 쓰지 않으므로 이 걱정이 없습니다.')
print('그래서 격자 문제의 안전한 기본값은 BFS입니다.')
