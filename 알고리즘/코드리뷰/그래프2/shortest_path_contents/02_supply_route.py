# 2단계: 응용 - 격자 다익스트라 (보급로 유형)
#
# 학습 목표
#   - 격자의 칸을 정점으로, 상하좌우 이동을 간선으로 보고 다익스트라를 쓸 수 있다.
#   - distance 를 2차원으로, 힙에 (거리, 행, 열) 을 넣을 수 있다.
#   - 오른쪽·아래로만 가는 방법으로는 풀 수 없는 경우가 있음을 이해한다.
#
# 문제
#   N x N 격자의 각 칸에 0 ~ 9 의 복구 비용이 적혀 있습니다. 왼쪽 위에서 오른쪽 아래까지
#   상하좌우로 한 칸씩 움직입니다. 어떤 칸에 들어갈 때마다 그 칸의 비용을 냅니다.
#   출발 칸과 도착 칸의 비용은 0 입니다. 드는 비용의 최솟값을 구하세요.
#
# 02_input.txt
#   첫 줄에 테스트 케이스 수 T
#   케이스마다 첫 줄에 N, 그 아래 N 줄에 숫자 N 개가 공백 없이 붙어 있음

import heapq
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '02_input.txt')

INF = float('inf')
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def min_cost(grid, n):
    # [실습 1]
    # 1-1. n x n 크기의 distance 를 만들고 모든 칸을 INF 로 채우세요.
    #      [[INF] * n] * n 은 안 됩니다. 같은 줄 하나를 n 번 가리키게 됩니다.
    distance = [[INF] * n for _ in range(n)]  # TODO

    # 1-2. 출발 칸 (0, 0) 의 거리는 0 입니다.
    distance[0][0] = 0  # TODO

    heap = [(0, 0, 0)]  # (누적거리, 행, 열)

    # 다익스트라 + 델타
    while heap:
        current_dist, row, col = heapq.heappop(heap)

        # [실습 2] 가지치기: 기록이 이미 더 짧으면 옛날 정보이니 건너뛰세요.
        if distance[row][col] < current_dist:  # TODO
            continue

        for k in range(4):
            nr = row + dr[k]
            nc = col + dc[k]

            # [실습 3]
            # 3-1. (nr, nc) 가 격자 안인지 확인하세요. 범위 밖이면 이 방향은 건너뜁니다.
            #      -1 은 파이썬에서 '맨 끝 칸' 이라 에러 없이 엉뚱한 칸을 보게 됩니다.
            if 0 <= nr < n and 0 <= nc < n:  # TODO
                new_dist = current_dist + grid[nr][nc]  # 들어가는 칸의 비용을 더한다

                # 3-2. new_dist 가 기록보다 짧으면 기록을 고치고, (new_dist, nr, nc) 를 힙에 넣으세요.
                if new_dist < distance[nr][nc]:  # TODO
                    distance[nr][nc] = new_dist # TODO
                    heapq.heappush(heap, (new_dist, nr, nc))

    print(distance)
    return distance[n - 1][n - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]
    print(f'#{tc} {min_cost(grid, N)}')

print('(정답: #1 5, #2 9)')
