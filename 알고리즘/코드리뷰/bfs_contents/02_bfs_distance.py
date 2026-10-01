# 2단계: BFS 최단 거리 + 경로 복원 + 비연결 그래프
#
# 학습 목표
#   - 방문 순서를 기록하던 자리를 거리 배열로 바꿀 수 있다.
#   - BFS 방문 순서가 왜 거리 오름차순과 같은지 설명할 수 있다.
#   - dist 배열 하나가 visited 역할까지 겸한다는 것을 안다.

import sys
from collections import deque
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '02_input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    node1 = data[i * 2]
    node2 = data[i * 2 + 1]

    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

for i in range(1, V + 1):
    adj_list[i].sort()

print(adj_list)

# ------------------------------------------------------------
# [실습 1] 최단 거리 구하기
# ------------------------------------------------------------
def bfs_distance(start_node, V, adj):
    """start_node에서 각 노드까지의 최단 거리(간선 수)를 돌려준다."""
    # dist[x] == -1 이 곧 '아직 방문 안 함' 입니다. visited 배열이 따로 없습니다.
    dist = [-1] * (V + 1)

    # 1-1. 시작 노드의 거리를 정하고 큐에 넣으세요.
    #      시작점에서 시작점까지의 거리는 몇일까요?
    queue = deque()
    dist[start_node] = 0  # TODO
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()

        for next_node in adj[current_node]:
            if dist[next_node] == -1:
                # 1-2. 이 노드까지의 거리를 정하고 큐에 넣으세요.
                #      부모까지의 거리에 몇을 더하면 될까요?
                dist[next_node] = dist[current_node] + 1  # TODO
                queue.append(next_node)

    return dist


dist = bfs_distance(1, V, adj_list)
print(dist) # dist 확인용

print('=== 1번에서 각 노드까지의 최단 거리 ===')
for i in range(1, V + 1):
    print(f'  {i}번: {dist[i]}')
print('  (정답: 1번 0, 2번 1, 3번 1, 4번 2, 5번 2, 6번 3, 7번 2)')
print()


# ------------------------------------------------------------
# [실습 2] 경로까지 복원하기
# ------------------------------------------------------------
def bfs_with_path(start_node, V, adj):
    """거리와 함께 '누구를 거쳐서 왔는지'(parent)도 기록한다."""
    dist = [-1] * (V + 1)
    parent = [0] * (V + 1)
    dist[start_node] = 0
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()

        for next_node in adj[current_node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[current_node] + 1

                # 2-1. next_node 에 '누구를 거쳐서 왔는지' 를 기록하세요.
                parent[next_node] = current_node # TODO
                queue.append(next_node)

    return dist, parent


def build_path(target, parent):
    """도착점에서 parent 를 거슬러 올라간 뒤 뒤집으면 경로가 됩니다."""
    path = []
    current = target

    while current:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


dist, parent = bfs_with_path(1, V, adj_list)

print('=== 최단 경로 ===')
for i in range(1, V + 1):
    route = ' -> '.join(map(str, build_path(i, parent)))
    print(f'  {i}번: 거리 {dist[i]}  경로 {route}')
print('  (정답 예: 6번은 거리 3, 경로 1 -> 2 -> 4 -> 6)')
print()

# --- 동작 과정 시각화 (완성되어 있습니다) ---
print('=== 왜 BFS가 최단 거리를 주는가 ===')

visit_order = []
seen = [False] * (V + 1)
seen[1] = True
queue = deque([1])
while queue:
    current = queue.popleft()
    visit_order.append(current)
    for neighbor in adj_list[current]:
        if not seen[neighbor]:
            seen[neighbor] = True
            queue.append(neighbor)

by_distance = sorted(range(1, V + 1), key=lambda x: (dist[x], x))

print(f'  BFS 방문 순서 : {" ".join(map(str, visit_order))}')
print(f'  거리 오름차순 : {" ".join(map(str, by_distance))}')
print('  => 실습을 마치면 두 줄이 완전히 일치합니다.')
print()
print('  BFS는 거리 0인 노드 -> 거리 1인 노드들 -> 거리 2인 노드들 순으로 훑습니다.')
print('  어떤 노드에 처음 도달했을 때가 항상 가장 가까운 경로이므로,')
print('  한 번 적은 거리는 나중에 고칠 일이 없습니다.')
print()

sys.setrecursionlimit(10**6)
dfs_order = []
seen = [False] * (V + 1)


def dfs(node):
    seen[node] = True
    dfs_order.append(node)
    for neighbor in adj_list[node]:
        if not seen[neighbor]:
            dfs(neighbor)


dfs(1)

print(f'  DFS 방문 순서 : {" ".join(map(str, dfs_order))}')
print('  6번은 실제로 가장 먼 노드(거리 3)인데 DFS에서는 4번째로 방문됩니다.')
print('  => DFS 방문 순서는 거리와 아무 관계가 없습니다.')
print()
print('주의: BFS가 최단 거리를 보장하는 것은 간선의 가중치가 모두 같을 때뿐입니다.')
print('      간선마다 비용이 다르면 다익스트라를 써야 합니다.')
print()

# ------------------------------------------------------------
# [실습 3] 비연결 그래프
# ------------------------------------------------------------
# 위에서는 bfs(1) 한 번만 호출했습니다. 모든 정점이 1번에서 도달 가능하다는 가정입니다.
# 아래처럼 끊겨 있으면 1번에서 출발해도 4, 5, 6 은 영원히 못 만납니다.
#
#   1 - 2        4 - 5
#    \                \
#     3                6
print('=== 비연결 그래프 ===')
V2 = 6
adj_broken = [[], [2, 3], [1], [1], [5], [4, 6], [5]]

reached = bfs_distance(1, V2, adj_broken)
found = [i for i in range(1, V2 + 1) if reached[i] != -1]
print(f'  bfs(1) 한 번만 호출: 도달한 노드 {found}')
print('  -> 4, 5, 6 을 못 찾습니다')

visited2 = [False] * (V2 + 1)
component_count = 0

for start in range(1, V2 + 1):
    # 3-1. 모든 정점을 확인하되, 어떤 조건일 때만 새 탐색을 시작해야 할까요?
    #      조건을 잘못 두면 이미 찾은 덩어리를 또 세게 됩니다.
    if not visited2[start]:  # TODO
        component_count += 1
        members = []
        queue = deque([start])
        visited2[start] = True

        while queue:
            current = queue.popleft()
            members.append(current)
            for neighbor in adj_broken[current]:
                if not visited2[neighbor]:
                    visited2[neighbor] = True
                    queue.append(neighbor)

        print(f'  {component_count}번째 덩어리 시작점 {start} -> {members}')

print(f'  연결 요소(덩어리) 개수: {component_count}   <- 정답은 2 입니다')
print()
print('이 for 루프는 DFS 문서 2.3절과 완전히 같은 구조입니다. 탐색 함수만 바뀝니다.')
print('바깥 루프는 탐색 방법과 무관하다는 뜻입니다.')
