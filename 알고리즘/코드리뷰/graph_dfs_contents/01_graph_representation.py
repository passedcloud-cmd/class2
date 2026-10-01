# 1단계: 그래프의 표현 (인접 행렬 / 인접 리스트 / 간선 리스트)
#
# 학습 목표
#   - 간선 하나가 세 방식에 각각 어떻게 저장되는지 설명할 수 있다.
#   - 무향 그래프에서 '양방향' 처리를 왜 해야 하는지 설명할 수 있다.
#   - 왜 코딩 테스트에서 인접 리스트를 기본으로 쓰는지 근거를 댈 수 있다.
#
# 시간 복잡도: 세 방식 모두 생성은 O(E)
# 공간 복잡도: 인접 행렬 O(V^2) / 인접 리스트 O(V + E) / 간선 리스트 O(E)

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '01_input.txt')

# 1. 입력 받기
V, E = map(int, input().split())  # 정점 7개, 간선 8개
data = list(map(int, input().split()))

print(f'정점 수 V = {V}, 간선 수 E = {E}')
print(f'간선 정보: {data}')
print()

# ------------------------------------------------------------
# [실습 1] 인접 행렬 (Adjacency Matrix)
# ------------------------------------------------------------
# 노드 번호가 1번부터 시작하므로 (V+1) x (V+1) 크기로 만들어 두었습니다.
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)] # 도화지

# 인접 행렬에 간선 그리기 (간선의 개수만큼)
for i in range(E):
    node1 = data[i * 2]
    node2 = data[i * 2 + 1]

    # node1 과 node2 가 연결되었음을 행렬에 1로 표시하세요.
    # 무향 그래프라는 점을 잊지 마세요. 표시할 칸이 하나가 아닙니다.
    adj_matrix[node1][node2] = 1 # TODO
    adj_matrix[node2][node1] = 1

print('=== 인접 행렬 ===')
print('    ' + ' '.join(f'{c}' for c in range(V + 1)))
for r in range(V + 1):
    print(f'{r} | ' + ' '.join(map(str, adj_matrix[r])))
print()
print(f'adj_matrix[1][2] = {adj_matrix[1][2]}  -> 1이면 1번과 2번이 연결된 것')
print(f'adj_matrix[1][4] = {adj_matrix[1][4]}  -> 0이면 연결되지 않은 것')
print()

# ------------------------------------------------------------
# [실습 2] 인접 리스트 (Adjacency List)
# ------------------------------------------------------------
adj_list = [[] for _ in range(V + 1)] # 빈리스트 만들기. 0번을 계속 비워두기 위해 V + 1개만큼 만듦

# 인접 리스트에 인접 정점 정보를 기록
for i in range(E):
    node1 = data[i * 2]
    node2 = data[i * 2 + 1]

    # 서로의 목록에 상대를 추가하세요. 여기도 양방향입니다.
    # TODO
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

print('=== 인접 리스트 ===')
print(adj_list)
for i in range(1, V + 1):
    print(f'{i}번과 연결된 노드: {adj_list[i]}')
print()

# ------------------------------------------------------------
# [실습 3] 간선 리스트 (Edge List)
# ------------------------------------------------------------
# (정점1, 정점2) 쌍을 그대로 모아 둡니다. 가중치가 있으면 (정점1, 정점2, 가중치).
# 크루스칼처럼 '간선을 정렬해서 하나씩 처리' 하는 알고리즘에서 씁니다.
# 여기는 양방향 처리를 하지 않습니다. 간선 하나가 항목 하나입니다.

# edge_list = [(data[i * 2], data[i * 2 + 1]) for i in range(E)]
edge_list = []
for i in range(E):
    edge_list.append((data[i * 2], data[i * 2 + 1]))

print('=== 간선 리스트 ===')
print(edge_list)
print()

# --- 동작 과정 시각화 (완성되어 있습니다) ---
print('=== 간선 하나가 세 방식에 어떻게 들어가는가 ===')
for i in range(3):
    node1 = data[i * 2]
    node2 = data[i * 2 + 1]
    print(f'간선 ({node1}, {node2})')
    print(f'  인접 행렬  -> [{node1}][{node2}] 와 [{node2}][{node1}] 에 1  (칸 2개)')
    print(f'  인접 리스트 -> {node1}번에 {node2}, {node2}번에 {node1}  (항목 2개)')
    print(f'  간선 리스트 -> ({node1}, {node2}) 하나만  (항목 1개)')
print()

print('=== 무엇을 쓸 것인가 ===')
print('구분            | 인접 행렬   | 인접 리스트  | 간선 리스트')
print('----------------|-------------|--------------|-------------')
print('공간 복잡도     | O(V^2)      | O(V + E)     | O(E)')
print('전체 탐색       | O(V^2)      | O(V + E)     | 부적합')
print('유리한 상황     | 조밀 그래프 | 대부분의 문제 | MST(간선 정렬)')
print()
print(f'이 그래프의 인접 행렬 칸 수 : {(V + 1) ** 2}')
print(f'이 그래프의 인접 리스트 항목: {sum(len(lst) for lst in adj_list)}')
print('=> 정점이 많아질수록 이 차이가 그대로 메모리 차이가 된다.')
