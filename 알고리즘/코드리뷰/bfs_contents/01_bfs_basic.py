# 1단계: BFS 기본 (인접 리스트 / 인접 행렬)
#
# 학습 목표
#   - BFS가 왜 큐(FIFO)와 짝인지 설명할 수 있다.
#   - 방문 처리를 '큐에 넣는 시점' 에 해야 하는 이유를 설명할 수 있다.
#   - 인접 리스트 정렬이 방문 순서에 어떤 영향을 주는지 안다.

import sys
from collections import deque
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '01_input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    node1 = data[i * 2]
    node2 = data[i * 2 + 1]

    adj_list[node1].append(node2)
    adj_list[node2].append(node1)
    adj_matrix[node1][node2] = 1
    adj_matrix[node2][node1] = 1

# 정렬 전 모습을 남겨 둔다. 아래 '실측 1' 에서 쓴다.
adj_unsorted = [lst[:] for lst in adj_list]

# 큐는 넣은 순서대로 나오므로, 작은 번호부터 방문하려면 오름차순으로 정렬한다.
for i in range(1, V + 1):
    adj_list[i].sort()

print('인접 리스트(오름차순):')
for i in range(1, V + 1):
    print(f'  {i}: {adj_list[i]}')
print()


# ------------------------------------------------------------
# [실습] 인접 리스트 + deque
# ------------------------------------------------------------
def bfs_list(start_node, V, adj):
    """start_node에서 출발해 가까운 노드부터 차례로 방문한다."""
    visited = [False] * (V + 1)
    path = []
    queue = deque()

    # 실습 1. 시작 노드를 방문 처리하고 큐에 넣으세요.
    #         이걸 채우기 전에는 while 루프가 아예 돌지 않아 경로가 비어 있습니다.
    visited[start_node] = True
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()
        path.append(current_node)

        for next_node in adj[current_node]:
            if not visited[next_node]:
                # 실습 2. 이 노드를 방문 처리하고 큐에 넣으세요.
                #         두 줄의 순서가 중요합니다. 큐에 넣기 '전에' 방문 처리해야
                #         같은 노드가 큐에 여러 번 쌓이지 않습니다.
                # TODO
                visited[next_node] = True
                queue.append(next_node)

    return path


# ------------------------------------------------------------
# 인접 행렬 + deque (완성되어 있습니다 - 위 실습의 참고용)
# ------------------------------------------------------------
def bfs_matrix(start_node, V, matrix):
    """알고리즘은 같고, 이웃을 찾는 방법만 다릅니다."""
    visited = [False] * (V + 1)
    path = []
    queue = deque()

    visited[start_node] = True
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()
        path.append(current_node)

        # 1번부터 V번까지 순서대로 훑으므로 별도 정렬 없이 작은 번호부터 방문합니다.
        for next_node in range(1, V + 1):
            if matrix[current_node][next_node] and not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return path


print(f'인접 리스트 + deque: {"".join(map(str, bfs_list(1, V, adj_list)))}')
print('   <- 정답은 1234576 입니다')
print(f'인접 행렬 + deque  : {"".join(map(str, bfs_matrix(1, V, adj_matrix)))}')
print('=> 두 결과가 같아야 합니다. 인접 행렬은 이웃을 찾으려고 매번 V칸을 훑습니다.')
print()

# --- 동작 과정 시각화 (완성되어 있습니다) ---
# 레벨별로 물결이 퍼지는 모습. 실습을 마친 뒤 방문 순서와 대조해 보세요.
print('=== 레벨별 확장 ===')
visited = [False] * (V + 1)
visited[1] = True
frontier = [1]
level = 0

while frontier:
    print(f'레벨 {level} | {frontier}')
    next_frontier = []

    for node in frontier:
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                next_frontier.append(neighbor)

    frontier = next_frontier
    level += 1

print('=> 한 겹씩 통째로 젖습니다. 이것이 돌멩이를 던졌을 때 퍼지는 물결입니다.')
print()

# --- 동작 과정 시각화 (완성되어 있습니다) ---
print('=== 큐 상태 추적 ===')
visited = [False] * (V + 1)
visited[1] = True
queue = deque([1])
path = []

while queue:
    current = queue.popleft()
    path.append(current)

    pushed = []
    for neighbor in adj_list[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)
            pushed.append(neighbor)

    print(
        f'  popleft {current} -> push {str(pushed):9s} | '
        f'큐 {str(list(queue)):15s} | 경로 {"".join(map(str, path))}'
    )
print()

# --- 실측 1: 정렬은 정말 필요한가? (완성되어 있습니다) ---
print('=== 실측 1: 인접 리스트 정렬의 효과 ===')
print(f'  정렬 O : {"".join(map(str, bfs_list(1, V, adj_list)))}')
print(f'  정렬 X : {"".join(map(str, bfs_list(1, V, adj_unsorted)))}')
print('  => 이 입력에서는 결과가 같습니다. 정렬을 지워도 정답이 나옵니다.')
print()

swapped = [1, 3, 1, 2] + data[4:]
adj_swapped = [[] for _ in range(V + 1)]
for i in range(E):
    adj_swapped[swapped[i * 2]].append(swapped[i * 2 + 1])
    adj_swapped[swapped[i * 2 + 1]].append(swapped[i * 2])
adj_swapped_sorted = [sorted(lst) for lst in adj_swapped]

print('  같은 그래프인데 간선 두 개의 순서만 바꾼 입력이라면?')
print(f'  정렬 X : {"".join(map(str, bfs_list(1, V, adj_swapped)))}')
print(f'  정렬 O : {"".join(map(str, bfs_list(1, V, adj_swapped_sorted)))}')
print('  => 정렬이 없으면 "입력에 적힌 순서" 대로 방문합니다.')
print('     문제에 "작은 번호부터" 조건이 있으면 정렬은 필수입니다.')
print()

# --- 실측 2: 방문 처리를 pop 시점에 하면? (완성되어 있습니다) ---
print('=== 실측 2: 방문 처리 시점 ===')


def count_pushes(size, mark_on_push, dense):
    """size 크기 그래프에서 큐에 총 몇 번 넣게 되는지 센다."""
    if dense:
        neighbors = [[v for v in range(size) if v != u] for u in range(size)]
    else:
        n = size
        neighbors = [[] for _ in range(n * n)]
        for r in range(n):
            for c in range(n):
                u = r * n + c
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        neighbors[u].append(nr * n + nc)

    total = len(neighbors)
    seen = [False] * total
    queue = deque([0])
    pushes = 1

    if mark_on_push:
        seen[0] = True

    while queue:
        current = queue.popleft()

        if not mark_on_push:
            if seen[current]:
                continue
            seen[current] = True

        for neighbor in neighbors[current]:
            if not seen[neighbor]:
                if mark_on_push:
                    seen[neighbor] = True
                queue.append(neighbor)
                pushes += 1

    return pushes


print('  4방향 격자 (희소 그래프)')
for n in (50, 100):
    ok = count_pushes(n, True, dense=False)
    bad = count_pushes(n, False, dense=False)
    print(f'    {n}x{n} | push 시점 {ok:7d} | pop 시점 {bad:7d} | {bad / ok:.1f}배')

print('  완전 그래프 (조밀 그래프)')
for n in (100, 500):
    ok = count_pushes(n, True, dense=True)
    bad = count_pushes(n, False, dense=True)
    print(f'    K_{n} | push 시점 {ok:7d} | pop 시점 {bad:7d} | {bad / ok:.0f}배')

print()
print('  => 격자에서는 2배 정도라 보통 "시간 초과" 로 먼저 걸립니다.')
print('     조밀 그래프에서는 정점 수에 비례해 불어나 "메모리 초과" 가 납니다.')
print('     어느 쪽이든, 방문 처리는 큐에 넣는 시점에 해야 합니다.')
