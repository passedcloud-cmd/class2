# V, E = 7, 8
# edge = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

# # 인접 리스트
# adj_list = [[] for _ in range(V+1)]
# for i in range(E):
#     node1, node2 = edge[i*2], edge[i*2+1]
#     adj_list[node1].append(node2)
#     adj_list[node2].append(node1)
# # print(adj_list)

# # 방문체크
# visited = [False] * (V+1)
# path = []

# from collections import deque
# def bfs(start_node):
#     queue = deque()
#     queue.append(start_node)
#     visited[start_node] = True

#     while queue:
#         currnet_node = queue.popleft()
#         path.append(currnet_node)
#         for next_node in adj_list[currnet_node]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)

# bfs(1)
# result = ''.join(map(str, path))
# print(result) # 출력 1234576


V, E = 7, 8
edge = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

# 인접 리스트
adj_list = [[] for _ in range(V+1)]
for i in range(E):
    node1, node2 = edge[i*2], edge[i*2+1]
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)
# print(adj_list)

# 방문체크
visited = [False] * (V+1)
path = []

def bfs(start_node):
    queue = [start_node]
    front = 0
    visited[start_node] = True
    while front < len(queue):
        current_node = queue[front]
        front += 1
        path.append(current_node)
        for next_node in adj_list[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
bfs(1)
print(*path)
# # 출력 1234576