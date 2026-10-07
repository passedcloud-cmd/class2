# 1단계: 다익스트라 - 가장 가까운 곳부터 확정하기
#
# 학습 목표
#   - distance 를 무한대로 초기화하고, 시작 정점만 0 으로 둘 수 있다.
#   - 힙에서 꺼낸 정보가 옛날 정보이면 건너뛰는 가지치기를 쓸 수 있다.
#   - 거쳐 가는 길이 더 짧을 때 기록을 고치고 힙에 넣는 간선 완화를 쓸 수 있다.
#
# 문제
#   정점 V 개, 방향 간선 E 개인 그래프에서 시작 정점부터 모든 정점까지의 최단 거리를 구하세요.
#
# 01_input.txt
#   첫 줄에 V E, 둘째 줄에 시작 정점, 그 아래 E 줄에 '출발 도착 가중치'
#
# 노션 '최단 경로' 2장과 같은 그래프, 같은 코드입니다.

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
    # [실습 1]
    # 1-1. 모든 정점의 거리를 INF(아직 모름)로 초기화하세요. 정점은 1번부터 씁니다.
    #      지금처럼 0 으로 두면 어떤 길도 0 보다 짧지 않아서 아무것도 갱신되지 않습니다.
    distance = [0] * (V + 1)  # TODO

    # 1-2. 시작 정점까지의 거리는 0 입니다.
    pass  # TODO

    heap = [(0, start_node)]  # (출발점부터의 거리, 정점)

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        # [실습 2] 가지치기
        #   기록된 거리(distance[current_node])가 지금 꺼낸 거리보다 이미 짧다면,
        #   이건 힙에 남아 있던 옛날 정보입니다. 건너뛰세요.
        #   <= 로 쓰면 '기록과 같은 최신 정보' 까지 버리게 됩니다.
        if False:  # TODO
            continue

        for next_node, weight in adj_list[current_node]:
            new_dist = current_dist + weight

            # [실습 3] 간선 완화
            # 3-1. current_node 를 거쳐 가는 길(new_dist)이 기록보다 짧은지 확인하세요.
            if False:  # TODO
                # 3-2. 기록을 new_dist 로 고치고, (new_dist, next_node) 를 힙에 넣으세요. (두 줄)
                pass  # TODO

    return distance


result = dijkstra(start)
print('최단 거리 :', result[1:])
print('(정답: [0, 2, 5, 1, 2, 4])')
