V, E = 7, 8
edge = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 인접 리스트 만들기
adj_list = [[] for _ in range(V+1)]
for i in range(E):
    node1, node2 = edge[i*2], edge[i*2+1]
    adj_list[node1].append(node2)
    adj_list[node2].append(node1) # 무방향 그래프
for i in range(1, V+1):
    adj_list[i].sort()
# BFS 함수 만들기
from collections import deque
def bfs_list(start_node, V, adj_list):
    visited = [False] * (V+1)
    path = []
    queue = deque()
    visited[start_node] = True
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()
        path.append(current_node)
        for next_node in adj_list[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
    return path
result_path = bfs_list(1, V, adj_list)
print(''.join(map(str, result_path))) #1234576
    