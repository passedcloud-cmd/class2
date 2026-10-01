# 0단계: BFS 백지에서 끝까지 써 보기
#
# 학습 목표
#   - BFS 코드를 아무것도 없는 상태에서 끝까지 써 본다.
#   - '그래프를 만든다 -> 그 위를 걸어 다닌다' 두 덩어리로 나눠서 생각한다.
#   - 내가 어디서 막히는지 스스로 찾아낸다. 막히는 지점이 곧 복습할 지점입니다.
#
# 순서
#   [0] 준비        import, 입력 파일 연결
#   [1] 그래프      V, E 읽기 -> 인접 리스트 만들기
#   [2] BFS 함수    방문 기록장 / 큐 / while 루프
#   [3] 실행과 출력
#
# 이 이름들을 그대로 쓰세요
#   V, E   data   adj_list   bfs_list   result_path
#
# 00_input.txt
#   7 8                               <- 정점 7개, 간선 8개
#   1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7   <- 두 개씩 짝지어 읽으면 간선 8개


# ============================================================
# [0] 준비
# ============================================================
import sys  # 0-1
from collections import deque  # 0-2
from pathlib import Path  # 0-3

BASE_DIR = Path(__file__).resolve().parent  # 0-4
sys.stdin = open(BASE_DIR / '00_input.txt')  # 0-5


# ============================================================
# [1] 그래프 만들기
# ============================================================
# 1-1. 첫 줄을 읽어 V, E 에 정수로 나눠 담으세요.
V, E = map(int, input().split())

# 1-2. 둘째 줄을 읽어 정수 리스트로 만들어 data 에 담으세요.
data = list(map(int, input().split()))

# 1-3. 비어 있는 리스트를 V + 1 개 가진 adj_list 를 만드세요.
#      +1 인 이유: 노드 번호가 1부터라 0번 자리를 하나 버리고 씁니다.
#      주의: [[]] * (V + 1) 로 만들면 안 됩니다. 한 리스트를 V+1번 가리키게 됩니다.

adj_list = [[] for _ in range(V+1)]

# 1-4. 간선 개수(E)만큼 도는 for 문을 여세요. 변수 이름은 i 로 합니다.
#      (1-5 와 1-6 은 이 for 안에 들어갑니다)
for i in range(E):

# 1-5. i번 간선의 두 끝을 node1, node2 에 담으세요.
#      data 는 두 개씩 짝입니다. 0번 간선은 data[0] 과 data[1] 입니다.
    node1, node2 = data[i*2], data[i*2+1]

# 1-6. 두 노드를 서로의 리스트에 넣으세요. 두 줄입니다.
#      방향이 없는 그래프라 양쪽 모두에 넣어야 합니다.
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

# 1-7. 1번부터 V번까지 각 리스트를 오름차순 정렬하세요. (for 한 줄 + 본문 한 줄)
#      큐는 넣은 순서대로 나오므로, 작은 번호부터 방문하려면 미리 정렬해 둡니다.
    
for i in range(1, V+1):
    adj_list[i].sort()

# 1-8. 잘 만들어졌는지 adj_list 를 출력해 보세요. 확인했으면 지워도 됩니다.
#      1번은 [2, 3], 6번은 [4, 5, 7] 이 나와야 합니다.
print(adj_list)

# ============================================================
# [2] BFS 함수
# ============================================================
# 2-1. bfs_list 라는 함수를 정의하세요.
#      매개변수는 순서대로 start_node, V, adj_list 세 개입니다.
#      (2-2 부터 2-13 까지는 전부 이 함수 안입니다. 들여쓰기에 주의하세요)
def bfs_list(start_node, V, adj_list):

    # 2-2. 방문 여부를 기록할 visited 를 만드세요. 전부 False, 길이는 V + 1 입니다.
    visited = [False] * (V+1)

    # 2-3. 방문한 순서를 쌓을 빈 리스트 path 를 만드세요.
    path = []

    # 2-4. 비어 있는 큐 queue 를 만드세요.
    queue = deque()

    # 2-5. 시작 노드를 방문했다고 표시하세요.
    # DFS는 pop 시점에서 방문 처리, BFS는 append 시점에서 방문 처리
    visited[start_node] = True

    # 2-6. 시작 노드를 큐에 넣으세요.
    queue.append(start_node)

    # 2-7. 큐가 비어 있지 않은 동안 반복하는 while 문을 여세요.
    #      빈 큐는 그 자체로 거짓이라 len() 을 쓰지 않아도 됩니다.
    #      (2-8 부터 2-12 까지는 이 while 안입니다)
    while queue:  # 큐가 빌 때까지 == 더 이상 갈 곳이 없을 때까지
        # 2-8. 큐의 가장 앞에서 노드를 꺼내 current_node 에 담으세요.
        #      뒤가 아니라 '앞' 입니다. 먼저 넣은 것이 먼저 나와야 너비 우선이 됩니다.
        current_node = queue.popleft()

        # 2-9. 꺼낸 노드를 path 에 기록하세요.
        path.append(current_node)

        # 2-10. current_node 와 이어진 노드들을 도는 for 문을 여세요.
        #       대상은 adj_list[current_node], 변수 이름은 next_node 로 합니다.
        for next_node in adj_list[current_node]:
            # 2-11. next_node 를 아직 방문하지 않았다면, 이라는 if 문을 여세요.
            if not visited[next_node]:
                # 2-12. 방문했다고 표시하고, 큐에 넣으세요. 두 줄입니다.
                #       [가장 중요] 표시가 먼저입니다. 꺼낼 때 표시하면 같은 노드가 큐에 여러 번 쌓입니다.
                visited[next_node] = True
                queue.append(next_node)

    # 2-13. 함수 맨 끝에서 path 를 돌려주세요. while 밖, 함수 안입니다.
    return path


# ============================================================
# [3] 실행과 출력
# ============================================================
# 3-1. 1번에서 출발하도록 bfs_list 를 부르고, 돌려받은 값을 result_path 에 담으세요.
result_path = bfs_list(1, V, adj_list)

# 3-2. result_path 의 숫자를 사이에 아무것도 넣지 않고 이어 붙여 출력하세요.
#      [1, 2, 3] 이라면 123 이 찍혀야 합니다. 숫자라서 그냥은 안 붙습니다.
print(''.join(map(str, result_path)))


# --- 정답 확인 (고치지 마세요) ---
if 'result_path' in globals():
    answer = ''.join(map(str, result_path))
    print('통과' if answer == '1234576' else '틀렸습니다. 정답은 1234576')
else:
    print('result_path 가 아직 없습니다. [3] 까지 완성하고 다시 실행하세요.')

