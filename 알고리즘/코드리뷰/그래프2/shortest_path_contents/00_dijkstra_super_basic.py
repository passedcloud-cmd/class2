# 0단계: 다익스트라 백지에서 끝까지 써 보기
#
# 학습 목표
#   - 그래프 입력부터 최단 거리 출력까지 아무것도 없는 상태에서 끝까지 써 본다.
#   - '꺼낸다 -> 옛날 정보면 버린다 -> 이웃을 고친다' 세 단계로 나눠서 생각한다.
#   - 내가 어디서 막히는지 스스로 찾아낸다. 막히는 지점이 곧 복습할 지점입니다.
#
# 순서
#   [0] 준비            import, 입력 파일 연결
#   [1] 그래프 만들기    인접 리스트, 중간 출력으로 확인
#   [2] 출발 준비        distance, heap
#   [3] 다익스트라 반복
#   [4] 결과 출력
#
# 이 이름들을 그대로 쓰세요 (맨 아래 정답 확인이 이 이름을 찾습니다)
#   V   E   start   adj_list   INF   distance   heap
#
# 00_input.txt
#   5 8        <- 정점 5개(1번 ~ 5번), 방향 간선 8개
#   1          <- 시작 정점
#   1 2 4      <- 1번에서 2번으로 가는 길, 거리 4
#   1 3 1
#   3 2 2
#   2 4 1
#   3 4 5
#   4 5 3
#   3 5 7
#   2 5 6


# ============================================================
# [0] 준비
# ============================================================
import heapq  # 0-1
import sys  # 0-2
from pathlib import Path  # 0-3

BASE_DIR = Path(__file__).resolve().parent  # 0-4
sys.stdin = open(BASE_DIR / '00_input.txt')  # 0-5


# ============================================================
# [1] 그래프 만들기
# ============================================================
# 1-1. 첫 줄을 읽어 V, E 에 정수로 나눠 담으세요.
V, E = map(int, input().split())
# 1-2. 둘째 줄을 읽어 start 에 정수로 담으세요.
start = int(input())
# 1-3. adj_list 를 만드세요. 정점마다 빈 리스트 하나씩, 0번 자리를 버리고 V + 1 칸입니다.
#      [[]] * (V + 1) 은 안 됩니다. 빈 리스트 하나를 V + 1 번 가리키게 됩니다.
adj_list = [[] for _ in range(V + 1)]
# 1-4. E 번 도는 for 문을 여세요. (1-5, 1-6 은 이 안입니다)
for _ in range(E):
    # 1-5. 한 줄을 읽어 node1, node2, weight 에 정수로 나눠 담으세요.
    node1, node2, weight = map(int, input().split())
    # 1-6. adj_list[node1] 에 (node2, weight) 를 넣으세요. 방향 그래프라 한쪽만 넣습니다.
    adj_list[node1].append((node2, weight))

# 1-7. adj_list 를 출력해 보세요. 이렇게 나와야 합니다.
#      [[], [(2, 4), (3, 1)], [(4, 1), (5, 6)], [(2, 2), (4, 5), (5, 7)], [(5, 3)], []]
print(adj_list)

# ============================================================
# [2] 출발 준비
# ============================================================
# 2-1. INF 에 무한대를 담으세요. float('inf') 를 씁니다.
INF = float('inf')
# 2-2. distance 를 만드세요. V + 1 칸 모두 INF 입니다. (아직 아무 데도 못 가 봤다)
distance = [INF] * (V + 1)
# 2-3. 시작 정점의 거리를 0 으로 바꾸세요.
distance[start] = 0
# 2-4. heap 을 (0, start) 하나만 든 리스트로 만드세요.
#      튜플의 첫 칸이 거리여야 힙이 '가까운 것부터' 꺼내 줍니다.
heap = [(0,start)]

# ============================================================
# [3] 다익스트라 반복
# ============================================================
# 3-1. heap 이 빌 때까지 도는 while 문을 여세요. (3-2 부터 끝까지 이 안입니다)
while heap:
    # 3-2. heap 에서 하나 꺼내 current_dist, current_node 에 나눠 담으세요.
    current_dist, current_node = heapq.heappop(heap)
    # 3-3. 기록된 거리(distance[current_node])가 current_dist 보다 이미 짧으면
    #      힙에 남아 있던 옛날 정보입니다. continue 로 건너뛰세요. 두 줄입니다.
    # 가지치기
    if distance[current_node] < current_dist: #지금 온 것보다 과거의 기록이 더 짧으면 기록 안 하고 그냥 넘어감
        continue

    # 3-4. current_node 의 이웃을 하나씩 보는 for 문을 여세요. (next_node, weight 로 받습니다)
    #      (3-5 부터 3-8 까지는 이 for 문 안입니다)
    for next_node, weight in adj_list[current_node]:

        # 3-5. current_node 를 거쳐 next_node 로 가는 거리를 new_dist 에 담으세요.
        # 누적된 경로
        new_dist = current_dist + weight

        # 3-6. new_dist 가 distance[next_node] 보다 짧은지 확인하는 if 문을 여세요.
        #      (3-7, 3-8 은 이 if 문 안입니다)
        if new_dist < distance[next_node]:
            # 3-7. distance[next_node] 를 new_dist 로 고치세요.
            distance[next_node] = new_dist
            # 3-8. (new_dist, next_node) 를 heap 에 넣으세요.
            heapq.heappush(heap, (new_dist, next_node))

# ============================================================
# [4] 결과 출력
# ============================================================
# 4-1. distance 를 1번 칸부터 출력하세요.
print(distance[1:])

# --- 정답 확인 (고치지 마세요) ---
if 'distance' in globals():
    print(
        '통과'
        if distance[1:] == [0, 3, 1, 4, 7]
        else '틀렸습니다. 정답은 [0, 3, 1, 4, 7]'
    )
else:
    print('distance 가 아직 없습니다. [2] 까지 완성하고 다시 실행하세요.')
