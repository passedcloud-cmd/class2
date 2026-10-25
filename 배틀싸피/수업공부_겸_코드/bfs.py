# ##### BFS 기본 #####
# V, E = 7, 8
# edge = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# # 인접 리스트 만들기
# adj_list = [[] for _ in range(V+1)]
# for i in range(E):
#     node1, node2 = edge[i*2], edge[i*2+1]
#     adj_list[node1].append(node2)
#     adj_list[node2].append(node1) # 무방향 그래프
# for i in range(1, V+1):
#     adj_list[i].sort()
# # BFS 함수 만들기
# from collections import deque
# def bfs_list(start_node, V, adj_list):
#     visited = [False] * (V+1)
#     path = []
#     queue = deque()
#     visited[start_node] = True
#     queue.append(start_node)

#     while queue:
#         current_node = queue.popleft()
#         path.append(current_node)
#         for next_node in adj_list[current_node]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
#     return path
# result_path = bfs_list(1, V, adj_list)
# print(''.join(map(str, result_path))) #1234576





# ##### bfs 시작점에서 각 노드까지의 최단 거리 & 경로 #####
# V, E = 7, 8
# edge = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# # 인접 리스트 만들기
# adj_list = [[] for _ in range(V+1)]
# for i in range(E):
#     node1, node2 = edge[i*2], edge[i*2+1]
#     adj_list[node1].append(node2)
#     adj_list[node2].append(node1) # 무방향 그래프
# for i in range(1, V+1):
#     adj_list[i].sort()

# from collections import deque
# def bfs_distance_path(start_node, V, adj):
#     dist = [-1]* (V + 1)
#     parent = [0] * (V + 1)
#     queue = deque()
#     dist[start_node] = 0
#     queue.append(start_node)

#     while queue:
#         current_node = queue.popleft()
#         for next_node in adj_list[current_node]:
#             if dist[next_node] == -1:
#                 dist[next_node] = dist[current_node] + 1
#                 parent[next_node] = current_node
#                 queue.append(next_node)

#     return dist, parent

# def build_path(target, parent):
#     path = []
#     current = target

#     while current:
#         path.append(current)
#         current = parent[current]
    
#     path.reverse()
#     return path

# dist, parent = bfs_distance_path(1, V, adj_list)
# print(f'시작 노드에서 각 노드까지 최단 거리: {dist}')
# print(f'부모 노드: {parent}')
# for i in range(1, V+1):
#     print(f'{i}번: 거리 {dist[i]} 경로 {build_path(i, parent)}')


# ##### bfs 미로 최단 거리 #####
# N, M = 4, 6
# maze = [[1,0,1,1,1,1],
#         [1,0,1,0,1,0],
#         [1,0,1,0,1,1],
#         [1,1,1,0,1,1],
#         ]

# dr = [-1, 1, 0, 0] #상하좌우
# dc = [0, 0, -1, 1]

# from collections import deque
# dist = [[-1] * M for _ in range(N)]
# dist[0][0]= 0
# queue = deque([(0, 0)])

# while queue:
#     r, c = queue.popleft()
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M:
#             if maze[nr][nc] == 1 and dist[nr][nc] == -1:
#                 dist[nr][nc] = dist[r][c] + 1
#                 queue.append((nr, nc))

# print(f'시작점 (0, 0) 에서 도착점 ({N - 1}, {M - 1}) 까지 최소 이동 횟수: {dist[N - 1][M - 1]}') #14





# ##### bfs 멀티 소스 #####
# N, M = 4, 6
# maze = [[1,0,1,1,1,1],
#         [1,0,1,0,1,0],
#         [1,0,1,0,1,1],
#         [1,1,1,0,1,1],
#         ]

# dr = [-1, 1, 0, 0] #상하좌우
# dc = [0, 0, -1, 1]

# sources = [(0,0), (N-1,M-1)]
# multi_dist = [[-1]*M for _ in range(N)]
# queue = deque()

# for sr, sc in sources:
#     multi_dist[sr][sc] = 0
#     queue.append((sr, sc))

# while queue:
#     r, c = queue.popleft()
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M:
#             if maze[nr][nc] == 1 and multi_dist[nr][nc] == -1:
#                 multi_dist[nr][nc] = multi_dist[r][c] + 1
#                 queue.append((nr, nc))

# print(f'시작점 {sources} 에서 동시에 퍼질 때, 각 칸까지의 거리')
# for row in multi_dist:
#     print(' '.join(f'{v:<3d}' for v in row))
#     # print(row)





# ##### bfs 섬 개수 찾기 #####
# N, M =5, 5
# grid = [[1,1,0,0,0],
#         [1,1,0,0,0],
#         [0,0,0,0,0],
#         [0,0,1,0,1],
#         [0,1,0,0,1],
#         ]

# dr = [-1, 1, 0, 0, -1, -1, 1, 1] #(상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
# dc = [0, 0, -1, 1, -1, 1, -1, 1]

# from collections import deque
# def bfs_islands(start_r, start_c, visited, directions):
#     queue = deque([(start_r, start_c)])
#     visited[start_r][start_c] = True
#     while queue:
#         r, c = queue.popleft()
#         for i in range(directions):
#             nr = r + dr[i]
#             nc = c + dc[i]

#             if 0 <= nr < N and 0 <= nc < M:
#                 if grid[nr][nc] == 1 and not visited[nr][nc]:
#                     visited[nr][nc] = True
#                     queue.append((nr, nc))

# def count_isands(directions):
#     visited = [[False] * M for _ in range(N)]
#     count = 0

#     for r in range(N):
#         for c in range(M):
#             if grid[r][c] == 1 and not visited[r][c]:
#                 count += 1
#                 bfs_islands(r,c, visited, directions)

#     return count

# print(f'8방향: 섬 {count_isands(8)}개') #3





# ##### 다익스트라1 #####
# # 간선에 가중치 있음. 가중치가 음수면 안됨. 시작점 정해짐. 
# V,E = 5, 8
# start = 1
# lst = [[1, 2, 4],
# [1, 3, 1],
# [3, 2, 2],
# [2, 4, 1],
# [3, 4, 5],
# [4, 5, 3],
# [3, 5, 7],
# [2, 5, 6],
# ] # 간선 정보 # (시작, 도착, 비용)

# import heapq
# adj_list = [[] for _ in range(V+1)]
# for i in range(E):
#     node1, node2, weight = lst[i][0], lst[i][1], lst[i][2]
#     adj_list[node1].append((node2, weight)) # (인접 노드, 비용)

# INF = float('inf')
# distance = [INF] * (V+1)
# distance[start] = 0 # 시작 정점의 거리는 0
# heap = [(0,start)] # heap에 시작점 넣고 시작
# while heap:
#     current_dist, current_node = heapq.heappop(heap)
#     # 가지치기
#     if current_dist > distance[current_node]:
#         continue
#     for next_node, weight in adj_list[current_node]:
#         new_dist = current_dist + weight
#         if new_dist < distance[next_node]:
#             distance[next_node] = new_dist
#             heapq.heappush(heap, (new_dist, next_node))

# print(f'지점별 도착 비용: {distance[1:]}') # [0, 3, 1, 4, 7]





# ##### 다익스트라2 #####
# N = 4
# arr = [[0,1,9,1],
#     [1,9,1,1],
#     [1,1,1,9],
#     [9,9,1,0],
#     ]

# import heapq
# INF = float('inf')
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]

# def min_cost(grid, n):
#     distance = [[INF] * n for _ in range(n)]
#     distance[0][0] = 0 # 시작점은 0
#     heap = [(0,0,0)] # 누적거리, 행, 열

#     while heap:
#         current_dist, row, col = heapq.heappop(heap)
#         if distance[row][col] < current_dist:
#             continue

#         for k in range(4):
#             nr = row + dr[k]
#             nc = col + dc[k]

#             if 0 <= nr < n and 0 <= nc <n:
#                 new_dist = current_dist + grid[nr][nc]

#                 if new_dist < distance[nr][nc]:
#                     distance[nr][nc] = new_dist
#                     heapq.heappush(heap, (new_dist, nr, nc))
#     print(f'지점 별 도착 비용: {distance}')
#     return distance[n-1][n-1]

# print(f'도착점까지 가는 데 필요한 최소 비용: {min_cost(arr, N)}') #1 5, #2 9





##### heapq 연습 #####
import heapq
heap = [5, 3, 8, 4, 1, 2]
heapq.heapify(heap) # 첫 번째 원소(heap[0])는 항상 가장 작은 값이 위치
# heappop으로 맨 앞(가장 작은 값)을 꺼내면, heapq가 나머지를 자동으로 정리해서 그다음으로 작은 값이 heap[0]에 와. # append나 pop을 쓰면 정리가 안 돼서 맨 앞이 가장 작은 값이라는 보장이 깨져.
print(f'heqp: {heap}')

small_first = []
while heap:
    pop_reuslt = heapq.heappop(heap) # heapq.heappop()은 가장 작은 값을 꺼냄
    small_first.append(pop_reuslt)
print(f'heapq 작은 순: {small_first}')
# -----------------------------
max_heap = []
numbers =[5, 3, 8, 4, 1, 2]
for number in numbers:
    heapq.heappush(max_heap, -number)

big_first = []
while max_heap:
    pop_reuslt = -heapq.heappop(max_heap)
    big_first.append(pop_reuslt)
print(f'heapq 큰 순: {big_first}')


patients = [('김철수', 2), ('이영희', 5), ('박민수', 3), ('최지우', 5), ('정하늘', 1)]
waiting = []
for order, (name, level) in enumerate(patients):
    heapq.heappush(waiting, (-level, order, name)) # 첫 번재 요소를 기준으로 삼음. 첫 번재 요소가 같으면 그 다음 요소 비교
call_order = []
while waiting:
    _, _, name = heapq.heappop(waiting)
    call_order.append(name)
print(f'환자 진찰 순서: {call_order}')

