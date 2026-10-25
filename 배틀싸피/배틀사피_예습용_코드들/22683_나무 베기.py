import sys
sys.stdin = open('22683_나무 베기.txt')
from collections import deque
# 상 우 하 좌(시계방향)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(grid, N, K, sr, sc, er, ec):
    """
    BFS로 최소 조작 횟수를 구하는 함수
    상태 : (행, 열, 방향, 나무 벤 횟수)
    조작: 전진A, 좌회전L, 우회전R 각각 1회
    """
    # 4차원 방문 배열: visited[행][열][방향4개][벤 횟수 0~K]
    visited = [[[[False] * (K+1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    # [False] * (K+1) for _ in range(4)]를 행의 개수로 한 겹 감싸고 다시 열의 개수로 한 겹 감싸서 4차원 방문 배열

    queue = deque()
    queue.append((sr, sc, 0,0,0)) #시작 위치, 위(0)를 보고, 나무 베기 0회, 조작 횟수 0회.
    visited[sr][sc][0][0] = True # 시작 상태 방문 처리

    while queue:
        r,c,d,cut,ops = queue.popleft()
        #목적지 도달 시 즉시 반환
        if r == er and c == ec:
            return ops

        # 새로운 r,c,d,cut,ops이 queue.popleft() 될 때마다 3가지 경우의 수로 갈래를 펼침
        # 조작1: 좌회전L
        nd = (d - 1) % 4 # 반시계 방향으로 90도 회전
        if not visited[r][c][nd][cut]:
            visited[r][c][nd][cut] = True
            queue.append((r,c,nd,cut, ops+1))

        # 조작 2: 우회전 R
        nd = (d+1) % 4
        if not visited[r][c][nd][cut]:
            visited[r][c][nd][cut] =True
            queue.append((r, c, nd, cut, ops+1))

        # 조작 3: 전진 A
        nr, nc = r +dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            # 평지G, 시작점X, 목적지Y 면 나무 안 베고 직진
            if grid[nr][nc] != 'T':
                if not visited[nr][nc][d][cut]:
                    visited[nr][nc][d][cut] = True
                    queue.append((nr, nc, d, cut, ops+1))
            else: # 나무
                # 벨 수 있는 횟수가 있다면 베고 전진
                new_cut = cut +1
                if new_cut <= K and not visited[nr][nc][d][new_cut]:
                    visited[nr][nc][d][new_cut] =True
                    queue.append((nr, nc, d, new_cut, ops+1))

    # 큐가 비었는데 목적지 도달 못함
    return -1

T = int(input())
for test_case in (1, 1+T):
    # N은 필드의 크기, K는 벨 수 있는 횟수
    N, K = map(int, input().split())
    grid = [list(map(str, input())) for _ in range(N)]

    # 시작 위치(X)와 목적지(Y)찾기
    sr, sc, er, ec = 0,0,0,0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'X':
                sr, sc = i, j
            elif grid[i][j] == 'Y':
                er, ec = i, j

    print(f'#{test_case} {bfs(grid, N, K, sr, sc, er, ec)}')



#1 7
#2 19