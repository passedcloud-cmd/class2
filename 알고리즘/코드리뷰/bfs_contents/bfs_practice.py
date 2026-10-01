V, E = 7, 8              
input_str ='1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
data = list(map(int, input_str.split()))

# 인접 리스트 만들기
# 빈 리스트 V+1개로 채워진 리스트 만들기. 0번재 인덱스는 비워둘 거라서 V+1개.
adj_list = [[] for _ in range(V+1)]

# 간선의 수만큼 반복하여 node1과 node2 연결 정보를 기록
for i in range(E):
    node1, node2 = data[i*2], data[i*2+1]
    adj_list[node1].append(node2)
    # 양방향 그래프니까 adj_list[node2]에도 node1 기록
    adj_list[node2].append(node1)

# adj_list의 각 리스트 요소들을 오름차순으로 정렬
for i in range(1, V+1):
    adj_list[i].sort()

# # deque 불러오기
from collections import deque

# bfs 함수 만들기
def bfs_list(start_node, V, adj_list):
    # 방문 기록지 만들기
    visited = [False] * (V+1)
    # 출력할 path 만들기
    path = []
    # deque로 queue 만들기
    queue = deque()

    # start_node를 방문 기록하고 queue에 넣기
    visited[start_node] = True
    queue.append(start_node)

    # queue가 빌 때까지 반복
    while queue:
        # queue에서 첫 번째 요소를 pop한 게 current_node
        current_node = queue.popleft()
        # current_node는 path에 넣기
        path.append(current_node)
        # 다음 노드 찾기
        for next_node in adj_list[current_node]:
            # next_node를 방문한 적이 없다면
            if not visited[next_node]:
                # 방문 기록하고
                visited[next_node] = True
                # queue에 추가
                queue.append(next_node)

    # path가 결과
    return path

result = bfs_list(1, V, adj_list)
print(''.join(map(str, result)))

from collections import deque





# 최단 거리 구하기
def bfs_distance(start_node, V, adj):
    # 거리를 기록. 방문 기록 겸임. -1이면 방문을 하지 않은 것
    dist = [-1] * (V + 1)

    queue = deque()
    # 시작점의 거리는 0
    dist[start_node] = 0 
    # 큐에 시작 노드 넣고 시작
    queue = deque([start_node])

    while queue:
        # 첫 번째 값이 current_node
        current_node = queue.popleft()
        # 다음 노드 확인
        for next_node in adj[current_node]:
            # 다음 노드를 방문한 적이 없다면
            if dist[next_node] == -1: 
                # 다음 노드의 거리는 현재 노드 + 1. 현재 노드와 이어져 있으니까.
                dist[next_node] = dist[current_node] + 1
                # 큐에 다음 노드 추가
                queue.append(next_node)
    return dist

result = bfs_distance(1, V, adj_list)
print(result)





# 미로 최단 거리 찾기

# 미로 준비
N, M = 4, 6
input_str ="101111 101010 101011 111011"
input_str1 = input_str.split()
maze = [[] for _ in range(len(input_str1))]
for i in range(len(input_str1)):
    maze[i] = list(map(int, input_str1[i]))
print(maze)
# 방향키 설정 - 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 거리를 기록할 dist 리스트
dist = [[-1] * (M) for _ in range(N)]
dist[0][0] = 0 # 시작점은 거리 0
queue = deque([(0, 0)])

while queue:
    r, c = queue.popleft()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            if maze[nr][nc] == 1 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

print(dist)




# 멀티 소스
sources = [(0, 0), (N-1, M-1)]
multi = [[-1] * M for _ in range(N)]
queue = deque()

for sr, sc in sources:
    multi[sr][sc] = 0
    queue.append((sr, sc))

while queue:
    r, c = queue.popleft()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            if maze[nr][nc] == 1 and multi[nr][nc] == -1:
                multi[nr][nc] = multi[r][c] + 1
                queue.append((nr, nc))


