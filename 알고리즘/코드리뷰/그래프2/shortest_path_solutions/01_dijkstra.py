# 1단계: 다익스트라 - 정답 코드

import heapq
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '01_input.txt')

INF = float('inf')

V, E = map(int, input().split())
start = int(input())

adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
    node1, node2, weight = map(int, input().split())
    adj_list[node1].append((node2, weight))  # 방향 그래프: node1 -> node2


def dijkstra(start_node):
    distance = [INF] * (V + 1)  # 1-1
    distance[start_node] = 0  # 1-2
    heap = [(0, start_node)]  # (출발점부터의 거리, 정점)

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        # 2. 가지치기: 이미 더 짧은 거리로 처리된 정점이면 건너뜀
        if distance[current_node] < current_dist:
            print(f'  건너뜀 ({current_dist}, {current_node})')
            continue

        print(f'확정 ({current_dist}, {current_node})')

        for next_node, weight in adj_list[current_node]:
            new_dist = current_dist + weight
            # 3-1. 이 정점을 거쳐 가는 길이 더 짧으면
            if new_dist < distance[next_node]:
                # 3-2. 기록을 고치고, 새 정보를 힙에 넣는다
                distance[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
                print(f'    {next_node} 갱신 -> {new_dist}')

        print(f'    distance = {distance[1:]}  heap = {heap}')

    return distance


result = dijkstra(start)
print('최단 거리 :', result[1:])
print()


# ============================================================
# 보조 자료 1 - 자주 내는 오답 세 가지
# ============================================================
def dijkstra_with_mistake(start_node, mistake):
    init = 0 if mistake == 'zero_init' else INF
    distance = [init] * (V + 1)
    distance[start_node] = 0
    heap = [(0, start_node)]
    pops = 0
    while heap:
        pops += 1
        if pops > 1000:
            return '무한 반복'
        current_dist, current_node = heapq.heappop(heap)
        if mistake == 'le_prune':
            skip = distance[current_node] <= current_dist
        else:
            skip = distance[current_node] < current_dist
        if skip:
            continue
        for next_node, weight in adj_list[current_node]:
            new_dist = current_dist + weight
            if mistake == 'reversed':
                better = new_dist > distance[next_node]
            else:
                better = new_dist < distance[next_node]
            if better:
                distance[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
    return distance[1:]


print('=== 보조 자료 1: 자주 나오는 오답 ===')
print('distance 를 0 으로 초기화 :', dijkstra_with_mistake(start, 'zero_init'))
print('가지치기를 <= 로          :', dijkstra_with_mistake(start, 'le_prune'))
print('비교 방향을 반대로        :', dijkstra_with_mistake(start, 'reversed'))
print('정답                      :', result[1:])
