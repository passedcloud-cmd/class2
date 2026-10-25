import sys
sys.stdin = open('5105_미로의 거리.txt')
from collections import deque
from collections import deque

# 상하좌우 4방향
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(start_r, start_c, N, maze):
    distance = [[0] * N for _ in range(N)]
    q = deque()
    q.append((start_r, start_c))
    # 시작점은 방문했으니까 1로 표시(이동횟수는 0)
    distance[start_r][start_c] =1
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0<= nr<N and 0 <=nc<N and maze[nr][nc] !=1 and distance[nr][nc] ==0:
                # 만약 다음 위치가 도착점(3이라면),
                if maze[nr][nc] ==3:
                    # 현재까지의 거리가 지나온 칸의 수
                    return distance[r][c] -1
                # 다음 위치의 거리를 (현재 위치 거리 +1)로 기록
                distance[nr][nc] = distance[r][c] +1
                q.append((nr, nc))

    # 큐가 모두 비워질 때까지 목적지를 찾지 못했다면 경로가 없는 것
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze =[list(map(int, input())) for _ in range(N)]

    # 미로에서 시작점(2) 찾기
    start_r, start_c = -1, -1
    for r in range(N):
        for c in range(N):
            if maze[r][c] ==2:
                start_r, start_c = r, c
                break

    result = bfs(start_r, start_c, N, maze)
    print(f'#{tc} {result}')
    


#1 5
#2 5
#3 0