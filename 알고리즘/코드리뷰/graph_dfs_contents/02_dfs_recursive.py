# 2단계: 재귀 DFS (인접 리스트 / 인접 행렬) + 비연결 그래프 처리
#
# 학습 목표
#   - 재귀 DFS의 첫 줄이 왜 반드시 방문 처리인지 설명할 수 있다.
#   - 인접 리스트 버전과 인접 행렬 버전의 차이를 코드로 구분할 수 있다.
#   - 그래프가 여러 덩어리로 끊겨 있을 때 무엇이 더 필요한지 설명할 수 있다.
#
# 시간 복잡도: 인접 리스트 O(V + E) / 인접 행렬 O(V^2)
# 공간 복잡도: visited O(V) + 재귀 호출 스택 최악 O(V)

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '02_input.txt')




# 세팅
# 재귀 깊이가 정점 수만큼 깊어질 수 있습니다. 기본 한계 1000은 금방 넘습니다.
# sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 인접 리스트와 인접 행렬에 간선 정보 채우기
for i in range(E):
    node1 = data[i * 2]
    node2 = data[i * 2 + 1]

    adj_list[node1].append(node2)
    adj_list[node2].append(node1)
    adj_matrix[node1][node2] = 1
    adj_matrix[node2][node1] = 1

# 인접 리스트는 정점 번호를 넣을 때 오른차순이나 내림차순을 고려해야 한다.
# 작은 번호부터 방문하려면 인접 리스트를 오름차순으로 정렬해 둡니다.
# 재귀는 리스트를 앞에서부터 꺼내 쓰므로 오름차순이 그대로 방문 순서가 됩니다.
for i in range(1, V + 1):
    adj_list[i].sort() # sort 매서드는 원본을 바꿈

print('인접 리스트(오름차순):')
for i in range(1, V + 1):
    print(f'  {i}: {adj_list[i]}')
print()

# 탐색
# ------------------------------------------------------------
# [실습 1] 인접 리스트 + 재귀
# ------------------------------------------------------------
def dfs_recursive_list(current, adj, visited, path): # current 하나만 넘겨주는 예시 코드도 있음
    # 1. 현재 노드를 방문 처리하고 path 에 기록하세요.
    #    이 두 줄이 함수의 '첫 줄' 이어야 합니다. 뒤로 미루면 무한 재귀에 빠집니다.
    # 2. adj[current] 를 순회하며, 아직 방문하지 않은 노드로 재귀 호출하세요.
    # TODO
    visited[current] = True # 1. 방문처리
    path.append(current) # 1. 최종 경로에 추가

    # 다음에 갈 곳은 어디인가?
    # 인접 리스트 표에서 현재 방문한 노드와 인접한 노드들이 누구인지 파악
    for next_node in adj[current]:
        # 꺼낸 순서 대로 방문하면 되나? No
        # 방문을 하지 않은 노드만 탐색을 다시 시작
        if visited[next_node] is False:
        # if not visited[next_node]: 로 써도 됨
            dfs_recursive_list(next_node, adj, visited, path)


# 방문 노드를 기록하는 기록지
visited = [False] * (V + 1) # 0번 노트 안 쓸 거니까 (V + 1) 개
# [False, False, False, False, False, False, False, False] # 어떤 노드를 방문했으면 True

# 방문한 노드를 순서대로 기록 (결과)
path = []
dfs_recursive_list(1, adj_list, visited, path)
print(f'인접 리스트 + 재귀: {"".join(map(str, path))}')


# ------------------------------------------------------------
# [실습 2] 인접 행렬 + 재귀
# ------------------------------------------------------------
def dfs_recursive_matrix(current, matrix, visited, path): 
    # 실습 1과 알고리즘은 완전히 같습니다. '다음 노드를 찾는 방법' 만 다릅니다.
    # 인접 리스트는 연결된 노드만 들어 있지만,
    # 인접 행렬은 1번부터 V번까지 전부 확인하면서 matrix[current][next_node] 가 1인지 봐야 합니다.
    # TODO
    visited[current] = True
    path.append(current)

    # 인접 행렬에서 현재 노드와 인접한 노드는 누구인지 찾고
    # 방문한 적이 없다면 탐색 이식
    for next_node in range(1, len(matrix)):
        if matrix[current][next_node] == 1 and not visited[next_node]:
            dfs_recursive_matrix(next_node, matrix, visited, path)




visited = [False] * (V + 1)
path = []
dfs_recursive_matrix(1, adj_matrix, visited, path)
print(f'인접 행렬 + 재귀  : {"".join(map(str, path))}')
print('=> 결과는 같아야 합니다. 다만 인접 행렬은 매번 V칸을 훑습니다. (O(V^2))')
print()

# ------------------------------------------------------------
# [실습 3] 비연결 그래프 다루기
# ------------------------------------------------------------
# 위에서는 dfs(1) 한 번만 호출했습니다. 이건 '모든 정점이 1번에서 도달 가능하다' 는 가정입니다.
# 아래처럼 그래프가 여러 덩어리로 끊겨 있으면 1번에서 출발해도 4, 5, 6 은 영원히 못 만납니다.
#
#   1 - 2        4 - 5
#    \                \
#     3                6
print('=== 비연결 그래프 ===')
V2 = 6 # 임의로 정점 설정
adj_broken = [[], [2, 3], [1], [1], [5], [4, 6], [5]] # 비연결 그래프를 인접 리스트로 표현

visited2 = [False] * (V2 + 1)
path2 = []
dfs_recursive_list(1, adj_broken, visited2, path2)
print(f'dfs(1) 한 번만 호출: {path2}  <- 4, 5, 6 을 못 찾습니다')

visited2 = [False] * (V2 + 1)
path2 = []
component_count = 0

for start in range(1, V2 + 1):
    # 모든 정점을 확인하되, 어떤 조건일 때만 '새 탐색' 을 시작해야 할까요?
    # 조건을 잘못 두면 이미 찾은 덩어리를 또 세게 됩니다.
    # 아직 방문하지 않은 정점이라면,
    if not visited2[start]:
        # 새로운 그래프라는 걸 카운팅하고 
        component_count += 1
        before = len(path2)
        dfs_recursive_list(start, adj_broken, visited2, path2)
        print(f'  {component_count}번째 덩어리 시작점 {start} -> {path2[before:]}')

print(f'전체 방문 경로: {path2}')
print(f'연결 요소(덩어리) 개수: {component_count}   <- 정답은 2 입니다')
print()
print('이 for 루프가 섬 찾기(04번)의 이중 for 루프와 완전히 같은 구조입니다.')
print('1차원 정점 목록이 2차원 격자로 바뀌었을 뿐입니다.')
print()

# --- 동작 과정 시각화 (완성되어 있습니다) ---
# 재귀가 어떻게 파고들고 되돌아 나오는지. 실습 1을 채운 뒤 결과를 대조해 보세요.
print('=== 재귀 호출 과정 ===')
visited = [False] * (V + 1)
trace = []


def dfs_trace(current, depth=0):
    pad = '  ' * depth
    visited[current] = True
    trace.append(current)
    print(f'{pad}dfs({current}) 진입 -> 방문 처리. 경로 {"".join(map(str, trace))}')

    for next_node in adj_list[current]:
        if visited[next_node]:
            print(f'{pad}  {next_node}: 이미 방문. 건너뜀')
        else:
            print(f'{pad}  {next_node}: 미방문 -> 파고든다')
            dfs_trace(next_node, depth + 1)

    print(f'{pad}dfs({current}) 종료 -> 부른 곳으로 되돌아간다')


dfs_trace(1)
