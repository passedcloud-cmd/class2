# 섬 준비
import sys
sys.stdin = open('04_input.txt')
N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

# 방문 여부
visited = [[False] * M for _ in range(N)]

#방향키 상 하 좌 우 상좌 상우 하좌 하우
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

# DFS 방식으로 하나의 섬 덩어리를 모두 방문 처리하는 함수 만들기
def dfs_recursive(start_x, start_y, direction):
    # 시작점 방문 처리로 시작
    visited[start_x][start_y] = True
    r, c = start_x, start_y
    
    # 다음 좌표 찾기
    for i in range(direction):
        nr = r + dr[i]
        nc = c + dc[i]

        # 경계 체크
        if 0 <= nr < N and 0 <= nc < M:
            # 다음 좌표가 땅이고, 방문한 적이 없다면
            if maps[nr][nc] == 1 and not visited[nr][nc]:
                # 다음 좌표를 방문 처리
                visited[nr][nc] = True
                # 다음 좌표에서 다시 DFS
                dfs_recursive(nr, nc, direction)

# 섬의 개수 카운트 0으로 시작
count = 0
# map을 완전 탐색
for i in range(M):
    for j in range(N):
        # 땅인 부분을 발견했고 방문한 적이 없다면 
        if maps[i][j] == 1 and not visited[i][j]:
            # 섬의 개수 카운트
            count += 1
            # dfs로 같은 섬 부분은 모두 방문 처리
            dfs_recursive(i, j, 8)

print(count)


from collections import deque
# BFS 방식으로 하나의 섬 덩어리를 모두 방문 처리하는 함수 만들기
def bfs_queue(start_x, start_y, direction):
    # 시작점을 방문 처리로 시작
    visited[start_x][start_y] = True
    # 큐 만들기
    queue = deque()
    # 큐에 시작점 넣기
    queue.append((start_x, start_y))

    # 큐가 빌 때까지 반복
    while queue:
        r, c = queue.popleft()

        # 다음 영역으로 이동
        for i in range(direction):
            nr = r + dr[i]
            nc = c + dc[i]

            # 경계체크
            if 0 <= nr < N and 0 <= nc < M:
                # 다음 영역이 땅이고 방문한 적이 없다면
                if maps[nr][nc] == 1 and not visited[nr][nc]:
                    # 방문 처리
                    visited[nr][nc] = True
                    # 큐에 넣기
                    queue.append((nr, nc))

# 섬 숫자 세기
cnt2 = 0

# 완전 탐색
for i in range(M):
    for j in range(N):
        # 만약 좌표가 땅이고 방문한 적이 없다면
        if maps[i][j] == 1 and not visited[i][j]:
            # 섬 개수를 세고 bfs 
            cnt2 += 1
            bfs_queue(i, j, 4)

print(cnt2)