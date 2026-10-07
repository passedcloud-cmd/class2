# 0단계: 다익스트라 백지에서 끝까지 써 보기 - 정답 코드
#
# 시간 복잡도: O(E log E) - 흔히 O(E log V) 로 적음
# 공간 복잡도: O(V + E)

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
V, E = map(int, input().split())  # 1-1
start = int(input())  # 1-2
adj_list = [[] for _ in range(V + 1)]  # 1-3
for _ in range(E):  # 1-4
    node1, node2, weight = map(int, input().split())  # 1-5
    adj_list[node1].append((node2, weight))  # 1-6
print(adj_list)  # 1-7

# ============================================================
# [2] 출발 준비
# ============================================================
INF = float('inf')  # 2-1
distance = [INF] * (V + 1)  # 2-2
distance[start] = 0  # 2-3
heap = [(0, start)]  # 2-4

# ============================================================
# [3] 다익스트라 반복
# ============================================================
while heap:  # 3-1
    current_dist, current_node = heapq.heappop(heap)  # 3-2
    if distance[current_node] < current_dist:  # 3-3
        print(f'  건너뜀 ({current_dist}, {current_node})')
        continue
    for next_node, weight in adj_list[current_node]:  # 3-4
        new_dist = current_dist + weight  # 3-5
        if new_dist < distance[next_node]:  # 3-6
            distance[next_node] = new_dist  # 3-7
            heapq.heappush(heap, (new_dist, next_node))  # 3-8

# ============================================================
# [4] 결과 출력
# ============================================================
print(distance[1:])  # 4-1


# --- 정답 확인 (고치지 마세요) ---
if 'distance' in globals():
    print(
        '통과'
        if distance[1:] == [0, 3, 1, 4, 7]
        else '틀렸습니다. 정답은 [0, 3, 1, 4, 7]'
    )
else:
    print('distance 가 아직 없습니다. [2] 까지 완성하고 다시 실행하세요.')
print()


# ============================================================
# 보조 자료 - 채점 주의 (2) 확인: 힙에 넣는 순서에 따라 꺼낸 횟수
# ============================================================
def count_pops(dist_first):
    dist = [INF] * (V + 1)
    dist[start] = 0
    h = [(0, start)] if dist_first else [(start, 0)]
    pops = 0
    while h:
        if dist_first:
            d, node = heapq.heappop(h)
        else:
            node, d = heapq.heappop(h)
        pops += 1
        if dist[node] < d:
            continue
        for nxt, w in adj_list[node]:
            if d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(h, (d + w, nxt) if dist_first else (nxt, d + w))
    return dist[1:], pops


print('=== 보조 자료: 힙 튜플 순서 비교 ===')
print('(거리, 정점) :', count_pops(True))
print('(정점, 거리) :', count_pops(False))
