import sys
sys.stdin = open('1226_미로1.txt')
from collections import deque

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(start_r, start_c):
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = True

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+ dr[i], c + dc[i]
            if 0 <= nr <16 and 0 <= nc < 16 and not visited[nr][nc]:
                if maze[nr][nc] ==3:
                    return 1

            # 다음 위치가 길0이라면 방문 처리 후 큐에 넣기
                if maze[nr][nc] ==0:
                    visited[nr][nc] = True
                    q.append((nr,nc))
    # q가 비워질 때까지 목적지 못 찾으면 경로 없음
    return 0

# 테스트 케이스 10개
for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[False]*16 for _ in range(16)]

    # 시작점을 찾아 BFS 시작
    # 그런데 항상 (1,1)에서 시작한다고 함
    start_r, start_c = 1, 1

    result = bfs(start_r, start_c)
    print(f'#{tc} {result}')

#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 1
#9 1
#10 1