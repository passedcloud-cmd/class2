# 3단계: 격자 BFS - 미로 최단 거리 + 멀티소스 BFS
#
# 학습 목표
#   - 격자를 그래프로 바꿔 볼 수 있다. (칸 = 정점, 이동 = 간선)
#   - 02번의 dist 배열이 격자에서 그대로 쓰인다는 것을 안다.
#   - 시작점이 여러 개일 때 무엇만 바뀌는지 설명할 수 있다.

import sys
from collections import deque
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '03_input.txt')

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

# 격자 문제는 대부분 4방향입니다. 지문에 '대각선' 이 있는지 먼저 확인하세요.
# 상, 하, 좌, 우 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

print('=== 입력 미로 ===')
for row in maze:
    print(''.join('.' if cell else '#' for cell in row))
print('(. = 길, # = 벽)')
print()

# ------------------------------------------------------------
# [실습 1] 미로 최단 거리
# ------------------------------------------------------------
# dist 배열이 visited 역할까지 겸합니다. -1 = 아직 도달 못 함.
# 출발점은 '아직 한 번도 안 움직인' 상태이므로 0부터 시작합니다.
# 02번의 dist 배열과 sentinel(-1) 까지 똑같습니다.
# (BOJ 2178처럼 '지나간 칸 수'를 묻는 문제라면 여기서 1부터 시작합니다. 지문 확인 필수)
dist = [[-1] * M for _ in range(N)]
print(dist)
dist[0][0] = 0
queue = deque([(0, 0)])

while queue:
    r, c = queue.popleft()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 1-1. 다음 칸 (nr, nc) 가 격자 범위 안이고, 길(1)이고, 아직 도달 전(-1)이라면
        #      거리를 기록하고 큐에 넣으세요.
        #      범위 확인을 먼저 해야 합니다. 순서를 바꾸면 IndexError 가 납니다.
        #
        # 조건은 if 두 개로 나눠도 되고, and 로 하나로 합쳐도 됩니다. 결과는 같습니다.
        # (린터 Ruff 는 합치는 쪽을 권합니다. SIM102)
        # 합쳐도 안전한 이유는 and 가 왼쪽이 거짓이면 오른쪽을 평가하지 않기 때문입니다.
        # TODO
        if 0 <= nr < N and 0 <= nc < M: #경계 안쪽
            if maze[nr][nc] == 1 and dist[nr][nc] == -1: # 다음칸이 길이고 방문한 적 없다면
                dist[nr][nc] = dist[r][c] + 1 # 다음 거리는 현재 거리 + 1
                queue.append((nr, nc)) 


print(f'(0, 0) 에서 ({N - 1}, {M - 1}) 까지 최소 이동 횟수: {dist[N - 1][M - 1]}')
print('   <- 정답은 14 입니다')
print()

# --- 동작 과정 시각화 (완성되어 있습니다) ---
print('=== 거리 배열 ===')
for row in dist:
    print(' '.join(f'{v:<3d}' for v in row))
print()
print('-1 은 벽이거나 도달하지 못한 칸입니다.')
print('실습 1을 채우면 왼쪽 위에서 출발한 숫자가 벽을 둘러 퍼져 나가는 것이 보입니다.')
print('=> 1장의 "물결이 퍼진다" 는 비유가 숫자로 그대로 나타난 것입니다.')
print()

print('=== 레벨별 확장 ===')
max_dist = max(max(row) for row in dist)
for step in range(max_dist + 1):
    cells = [(r, c) for r in range(N) for c in range(M) if dist[r][c] == step]
    print(f'  거리 {step:2d} : {cells}')
print()

# ------------------------------------------------------------
# [실습 2] 멀티소스 BFS (시작점이 여러 개)
# ------------------------------------------------------------
# 불이 여러 곳에서 번지거나, 익은 토마토가 여러 개 있거나,
# 바이러스가 여러 곳에서 퍼지는 유형입니다.
# 아래 while 루프는 실습 1과 글자 하나 다르지 않습니다. 바뀌는 건 시작 부분뿐입니다.
print('=== 멀티소스 BFS ===')

# 위쪽 미로 문제에서 '길'인 칸 중 4귀퉁이 쪽 두 곳에서 동시에 퍼진다고 가정
sources = [(0, 0), (N - 1, M - 1)] # 시작점 2개
multi = [[-1] * M for _ in range(N)]
queue = deque()

# 2-1. sources 에 담긴 시작점들을 전부 거리 0으로 기록하고 큐에 넣으세요.
#      한 곳만 넣는 것이 아니라 전부 넣는 것이 핵심입니다.
# TODO
for sr, sc in sources:
    multi[sr][sc] = 0
    queue.append((sr, sc)) # 시작점을 전부 미리 queue애 넣음


while queue:
    r, c = queue.popleft()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 경계를 넘지 않고
        if 0 <= nr < N and 0 <= nc < M:
            if maze[nr][nc] == 1 and multi[nr][nc] == -1: # 길이 있으며, 방문한 적 없으면
                multi[nr][nc] = multi[r][c] + 1 # 다음 길은 현재 위치의 + 1
                queue.append((nr, nc)) 

print(f'시작점 {sources} 에서 동시에 퍼질 때, 각 칸까지의 거리')
for row in multi:
    print(' '.join(f'{v:<3d}' for v in row))
print()
print('while 루프는 시작점이 하나일 때와 글자 하나 다르지 않습니다.')
print('큐를 여러 개로 채운 것이 전부입니다.')
print('=> BFS가 알아서 "가장 가까운 시작점까지의 거리" 를 칸마다 채워 줍니다.')
