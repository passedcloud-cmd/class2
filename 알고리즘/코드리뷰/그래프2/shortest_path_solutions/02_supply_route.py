# 2단계: 응용 - 격자 다익스트라 (보급로 유형) - 정답 코드

import heapq
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '02_input.txt')

INF = float('inf')
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def min_cost(grid, n):
    distance = [[INF] * n for _ in range(n)]  # 1-1
    distance[0][0] = 0  # 1-2. 출발 칸은 비용 0 (문제 조건)
    heap = [(0, 0, 0)]  # (거리, 행, 열)

    while heap:
        current_dist, row, col = heapq.heappop(heap)

        # 2. 가지치기
        if distance[row][col] < current_dist:
            continue

        for k in range(4):
            nr = row + dr[k]
            nc = col + dc[k]
            # 3-1. 격자 안인지 먼저 확인
            if 0 <= nr < n and 0 <= nc < n:
                # if 0 <= nr < n and 0 <= nc < n and new_dist < distance[nr][nc]: 로
                # 합쳐도 됩니다. and 는 앞이 False 면 뒤를 보지 않아서 범위 밖 접근이 없습니다.
                new_dist = current_dist + grid[nr][nc]
                # 3-2. 간선 완화
                if new_dist < distance[nr][nc]:
                    distance[nr][nc] = new_dist
                    heapq.heappush(heap, (new_dist, nr, nc))

    return distance[n - 1][n - 1]


T = int(input())
grids = []
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]
    grids.append(grid)
    print(f'#{tc} {min_cost(grid, N)}')
print()


# ============================================================
# 보조 자료 1 - 왜 DP / BFS 가 아니라 다익스트라인가
# ============================================================
def right_down_dp(grid, n):
    """오른쪽, 아래로만 움직인다고 가정한 DP"""
    dp = [[INF] * n for _ in range(n)]
    dp[0][0] = 0
    for r in range(n):
        for c in range(n):
            if r > 0:
                dp[r][c] = min(dp[r][c], dp[r - 1][c] + grid[r][c])
            if c > 0:
                dp[r][c] = min(dp[r][c], dp[r][c - 1] + grid[r][c])
    return dp[n - 1][n - 1]


def fewest_cells_cost(grid, n):
    """BFS 로 칸 수가 가장 적은 길을 찾고, 그 길의 비용을 돌려준다"""
    prev = [[None] * n for _ in range(n)]
    seen = [[False] * n for _ in range(n)]
    seen[0][0] = True
    queue = [(0, 0)]
    head = 0
    while head < len(queue):
        row, col = queue[head]
        head += 1
        for k in range(4):
            nr, nc = row + dr[k], col + dc[k]
            if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                seen[nr][nc] = True
                prev[nr][nc] = (row, col)
                queue.append((nr, nc))
    cost = 0
    cell = (n - 1, n - 1)
    while cell != (0, 0):
        cost += grid[cell[0]][cell[1]]
        cell = prev[cell[0]][cell[1]]
    return cost


print('=== 보조 자료 1: 같은 격자, 다른 방법 ===')
for tc, grid in enumerate(grids, start=1):
    n = len(grid)
    print(
        f'#{tc} 다익스트라 {min_cost(grid, n)} / 오른쪽·아래 DP {right_down_dp(grid, n)}'
        f' / BFS 최소 칸 수 길 {fewest_cells_cost(grid, n)}'
    )
