"""
[비유]
- prev = 발자국. 도착점에서 발자국을 거꾸로 따라가면 출발점이 나온다.
"""

# 3단계: 응용 - 최단 경로 복원하기 - 정답 코드

import heapq
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '03_input.txt')

INF = float('inf')

V, E = map(int, input().split())
start = int(input())

adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
    node1, node2, weight = map(int, input().split())
    adj_list[node1].append((node2, weight))


def dijkstra(start_node):
    distance = [INF] * (V + 1)
    prev = [0] * (V + 1)  # prev[v]: v 로 오는 최단 길에서 v 바로 앞 정점. 0 은 '없음'
    distance[start_node] = 0
    heap = [(0, start_node)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if distance[current_node] < current_dist:
            continue
        for next_node, weight in adj_list[current_node]:
            new_dist = current_dist + weight
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                prev[next_node] = current_node  # [실습 1] 거리를 고칠 때 발자국도 같이
                heapq.heappush(heap, (new_dist, next_node))

    return distance, prev


def get_path(prev, end_node):
    path = []
    node = end_node
    while node != 0:  # 2-1, 2-2. 시작 정점의 prev 는 0 이라 거기서 멈춘다
        path.append(node)
        node = prev[node]
    path.reverse()  # 2-3. 거꾸로 모았으니 뒤집기
    return path


distance, prev = dijkstra(start)
print('prev :', prev[1:])
for end in range(1, V + 1):
    path = get_path(prev, end)
    print(
        f'{start} -> {end} : 거리 {distance[end]}, 경로 {" -> ".join(map(str, path))}'
    )
print()


# ============================================================
# 보조 자료 1 - 동점일 때도 고치면(<=) 경로가 바뀐다
# ============================================================
def dijkstra_tie(start_node):
    distance = [INF] * (V + 1)
    prev_tie = [0] * (V + 1)
    distance[start_node] = 0
    heap = [(0, start_node)]
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if distance[current_node] < current_dist:
            continue
        for next_node, weight in adj_list[current_node]:
            new_dist = current_dist + weight
            if new_dist <= distance[next_node]:  # 같아도 고친다
                distance[next_node] = new_dist
                prev_tie[next_node] = current_node
                heapq.heappush(heap, (new_dist, next_node))
    return prev_tie


print('=== 보조 자료 1: < 와 <= 의 차이 ===')
print('<  일 때 3 번 경로 :', get_path(prev, 3))
print('<= 일 때 3 번 경로 :', get_path(dijkstra_tie(start), 3))
