# 4단계: 섬의 개수 세기 - DFS로 풀었던 문제를 BFS로
#
# 학습 목표
#   - 연결 요소 세기는 DFS든 BFS든 답이 같다는 것을 손으로 확인한다.
#   - 바깥 이중 for 루프와 탐색 함수의 역할이 어떻게 나뉘는지 설명할 수 있다.
#
# 힌트: graph_dfs_contents/04_island_count.py 를 옆에 띄워 놓고 비교하세요.
#       바깥 이중 for 루프는 글자 하나 바꿀 필요가 없습니다.

import sys
from collections import deque
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '04_input.txt')

N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

# 8방향 델타 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

for row in grid:
    print(''.join('■' if cell else '·' for cell in row))
print()


# ------------------------------------------------------------
# [실습 1] 섬 하나를 통째로 방문 처리하기
# ------------------------------------------------------------
def bfs_island(start_r, start_c, visited, directions):
    """(start_r, start_c) 와 이어진 땅을 전부 방문 처리합니다."""
    # 1-1. 시작 좌표를 담은 큐를 만들고, 시작 좌표를 방문 처리하세요.
    #      좌표는 (행, 열) 튜플 하나로 묶어서 넣습니다.
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True # TODO
    while queue:
        # 큐에서 하나를 꺼내면서 탐색 시작
        r, c = queue.popleft()

        # 현재 위치에서 8방향을 탐색
        for i in range(directions):
            nr = r + dr[i]
            nc = c + dc[i]

            # 1-2. (nr, nc) 가 격자 안이고, 땅(1)이고, 아직 방문 전이라면
            #      방문 처리하고 큐에 넣으세요.
            #      범위 확인이 먼저입니다. 순서를 바꾸면 IndexError 가 납니다.
            #      방문 처리는 '큐에 넣기 직전' 입니다.
            # TODO
            if 0 <= nr < N and 0 <= nc < M:
                if grid[nr][nc] == 1 and not visited[nr][nc]:
                    # 방문 처리 후 큐에 넣기
                    visited[nr][nc] = True
                    queue.append((nr, nc))


# ------------------------------------------------------------
# [실습 2] 섬 세기
# ------------------------------------------------------------
def count_islands(directions):
    """모든 칸을 훑으면서, 아직 방문하지 않은 땅을 만날 때마다 새 섬으로 셉니다."""
    visited = [[False] * M for _ in range(N)]
    count = 0

    # 지도 전체 탐색반
    for r in range(N):
        for c in range(M):
            # 2-1. 어떤 칸에서만 새 섬으로 세야 할까요? 조건 두 개가 필요합니다.
            #      이 두 줄(count += 1, bfs_island 호출)은 이미 써 두었습니다.
            # 일단 땅이어야 하고(1), 아직 방문하지 않았어야 한다(False).
            if grid[r][c] == 1 and not visited[r][c]: # TODO
                count += 1
                # 상륙부대 투입
                bfs_island(r, c, visited, directions)

    return count


print(f'8방향: 섬 {count_islands(8)}개   (정답 3)')
print(f'4방향: 섬 {count_islands(4)}개   (정답 4)')
print()
print('=> 대각선을 인정하느냐에 따라 답이 달라집니다.')
print('   델타 배열은 문제 지문을 읽고 정하는 것이지, 외워 두는 것이 아닙니다.')
print('=> 섬을 세는 일은 바깥 루프가, 번지는 일은 BFS가 합니다.')
print('   이 구조는 DFS로 바꿔도 그대로입니다. 탐색 함수만 갈아 끼우면 됩니다.')
