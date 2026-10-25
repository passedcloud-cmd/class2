# ##### dfs 회귀 #####
# V, E = 7, 8
# edge = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# adj_list = [[] for _ in range(V + 1)]
# for i in range(E):
#     node1 = edge[i * 2]
#     node2 = edge[i * 2 + 1]
#     adj_list[node1].append(node2)
#     adj_list[node2].append(node1)
# for i in range(1, V + 1):
#     adj_list[i].sort()

# def dfs_recursive_list(current, adj, visited, path):
#     visited[current] = True
#     path.append(current)

#     for next_node in adj[current]:
#         if visited[next_node] is False:
#             dfs_recursive_list(next_node, adj, visited, path)

# visited = [False] * (V + 1)
# path = []
# dfs_recursive_list(1, adj_list, visited, path)
# print(f'인접 리스트 + 재귀: {"".join(map(str, path))}')

# ### + 비연결 그래프 ###
# V2 = 6
# adj_broken = [[], [2, 3], [1], [1], [5], [4, 6], [5]]
# visited2 = [False] * (V2 + 1)
# path2 = []
# component_count = 0
# for start in range(1, V2 + 1):
#     if not visited2[start]:
#         # 새로운 그래프라는 걸 카운팅하고 
#         component_count += 1
#         before = len(path2)
#         dfs_recursive_list(start, adj_broken, visited2, path2)
#         print(f'  {component_count}번째 덩어리 시작점 {start} -> {path2[before:]}')






##### dfs 스택 #####

V, E = 7, 8
edge_input = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

adj_list = [[] for _ in range(V+1)]
for i in range(E):
    node1, node2 = edge_input[i*2], edge_input[i*2 + 1]
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)
for i in range(1, V+1):
    adj_list[i].sort(reverse=True) # 숫자가 작은 노드 먼저 방문하기 위해 내림차순 정렬

visited = [False] * (V + 1)
path = []
stack = []

def adj_list_stack_pop(start_node):
    stack.append(start_node)

    while stack:
        current_node = stack.pop()
        if not visited[current_node]:
            visited[current_node] = True
            path.append(current_node)
            for next_node in adj_list[current_node]:
                if not visited[next_node]:
                    stack.append(next_node)        

adj_list_stack_pop(1)
print(f'dfs 스택 결과: {''.join(map(str, path))}') #1246573




#### dfs 섬 개수 세기 #####
N, M =5, 5
grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,0,0],
        [0,0,1,0,1],
        [0,1,0,0,1],
        ]

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(r, c, visited):
    visited[r][c] = True 
    for i in range(8):  
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if grid[nr][nc] == 1 and not visited[nr][nc]:
                dfs(nr, nc, visited) 
                                
visited = [[False] * M for _ in range(N)]
island_count = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]:
            island_count += 1
            dfs(i, j, visited)

print(f'DFS 풀이 섬의 개수: {island_count}') #3