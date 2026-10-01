from collections import deque

V, E = 7, 8
txt = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
data = list(map(int, txt.split()))

adj_list = [[] for _ in range(V+1)]
for i in range(E):
    node1, node2 = data[i*2], data[i*2+1]
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

for i in range(1, V+1):
    adj_list[i].sort()

def bfs_distance(start_node, V, adj_list):
    dist = [-1] * (V+1)
    parent = [0] * (V+1)
    dist[start_node] = 0
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        for next_node in adj_list[current_node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[current_node] + 1
                parent[next_node] = current_node # 누구를 거쳐서 왔는지 기록
                queue.append(next_node)
    return dist, parent

def get_path(target, parent):
    path = []
    current = target
    while current: # current가 0이 될때까지 계속
        path.append(current)
        current = parent[current]
    path.reverse() # 도착점에서부터 시작했으니까 거꾸로 
    return path

dist, parent = bfs_distance(1, V, adj_list)

for i in range(1, V+1):
    path = get_path(i, parent)
    print(f'{i}번: {dist[i]}, 경로 {path}')




print('\n')
####### 미로 찾기 ######
# N은 세로 크기, M은 가로 크기
N, M = 4, 6
maze = [[1,0,1,1,1,1], [1,0,1,0,1,0], [1,0,1,0,1,1], [1,1,1,0,1,1]]

# 상 하 좌 우 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dist = [[-1] * M for _ in range(N)]
dist[0][0] = 0
queue = deque([(0,0)])

while queue:
    r, c = queue.popleft()

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            if maze[nr][nc] == 1 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

print(dist[N - 1][M - 1])








#### 멀티소스 BFS(시작점이 여러 개)
from collections import deque

# BOJ 7576 토마토: 첫 줄은 M(가로) N(세로) 순서로 들어온다
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
# 1 = 익은 토마토, 0 = 안 익은 토마토, -1 = 빈 칸

# 상 하 좌 우 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dist = [[-1] * M for _ in range(N)]
queue = deque()

# 1. 시작점(익은 토마토)을 전부 큐에 넣고 거리 0으로 세팅
for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            dist[r][c] = 0
            queue.append((r, c))

# 2. BFS: 시작점이 하나일 때와 구조가 같다
while queue:
    r, c = queue.popleft()

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if 0 <= nr < N and 0 <= nc < M: # 상자 안
            if maze[nr][nc] == 1 and dist[nr][nc] == -1: # 안 익었고 처음 가는 칸
                dist[nr][nc] = dist[r][c] + 1 # 하루 뒤에 익는다
                queue.append((nr, nc))


# 3. 결과 계산
answer = 0
for r in range(N):
    for c in range(M):
        if box[r][c] == 0 and dist[r][c] == -1:   # 끝까지 못 익은 토마토가 있으면
            print(-1)
            exit() # 당장 끝내라.
        answer = max(answer, dist[r][c])          # 가장 늦게 익은 날짜
 
print(answer)


