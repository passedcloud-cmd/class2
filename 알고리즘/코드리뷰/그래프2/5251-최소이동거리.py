import sys
sys.stdin = open('5251-최소이동거리.txt')

T = int(input())
for test_case in range(1, T+1):
    # N은 연결지점 번호, E는 도로의 개수
    N, E = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(E)]
    # print(lst)

    # 인접 리스트
    adj_list = [[] for _ in range(N+1)]
    for i in range(E):
        node1, node2, weight = lst[i][0], lst[i][1], lst[i][2]
        adj_list[node1].append((weight, node2))
    # print(adj_list) 

    # 최단 거리 리스트
    start = 0 
    INF = float('inf')
    distant = [INF] * (N+1)
    distant[start] = 0

    import heapq
    heap = [(0, start)] # heap에 시작점 넣고 시작

    # heap이 빌 때까지 반복
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        # 가지치기
        if current_dist > distant[current_node]:
            continue

        # 주변 노드 거리 계산
        for next_dist, next_node in adj_list[current_node]:
            new_dist = current_dist + next_dist
            if new_dist < distant[next_node]:
                distant[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    result = distant.pop()
    
    print(f'#{test_case} {result}')