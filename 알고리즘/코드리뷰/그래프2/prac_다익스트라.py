# #   5 8        <- 정점 5개(1번 ~ 5번), 방향 간선 8개
# #   1          <- 시작 정점
# #   1 2 4      <- 1번에서 2번으로 가는 길, 거리 4
# #   1 3 1
# #   3 2 2
# #   2 4 1
# #   3 4 5
# #   4 5 3
# #   3 5 7
# #   2 5 6

# # 5 8
# # 1
# # 1 2 4  
# # 1 3 1
# # 3 2 2
# # 2 4 1
# # 3 4 5
# # 4 5 3
# # 3 5 7
# # 2 5 6
# V,E = map(int, input().split()) # 정점, 간선 개수
# start = int(input())
# lst = [list(map(int,input().split())) for _ in range(E)] # 간선 정보 # (시작, 도착, 비용)
# # print(lst)

# import heapq
# # 인접 리스트 만들기
# adj_list = [[] for _ in range(V+1)]
# for i in range(E):
#     node1, node2, weight = lst[i][0], lst[i][1], lst[i][2]
#     adj_list[node1].append((node2, weight))
# print(adj_list)

# INF = float('inf')
# distance = [INF] * (V+1)
# distance[start] = 0 # 시작 정점의 거리는 0
# heap = [(0,start)] # heap에 시작점 넣고 시작
# while heap:
#     current_dist, current_node = heapq.heappop(heap)
#     # 가지치기
#     if current_dist > distance[current_node]:
#         continue
#     for next_node, weight in adj_list[current_node]:
#         new_dist = current_dist + weight
#         if new_dist < distance[next_node]:
#             distance[next_node] = new_dist
#             heapq.heappush(heap, (new_dist, next_node))

# print(distance[1:]) # [0, 3, 1, 4, 7]




# import heapq
# heap = [5, 3, 8, 4, 1, 2]
# heapq.heapify(heap)

# small_first = []
# while heap:
#     pop_reuslt = heapq.heappop(heap)
#     small_first.append(pop_reuslt)

# max_heap = []
# numbers =[5, 3, 8, 4, 1, 2]
# for number in numbers:
#     heapq.heappush(max_heap, -number)

# big_first = []
# while max_heap:
#     pop_reuslt = -heapq.heappop(max_heap)
#     big_first.append(pop_reuslt)

# print(small_first)
# print(big_first)

# patients = [('김철수', 2), ('이영희', 5), ('박민수', 3), ('최지우', 5), ('정하늘', 1)]
# waiting = []
# for order, (name, level) in enumerate(patients):
#     heapq.heappush(waiting, (-level, order, name)) # 첫 번재 요소를 기준으로 삼음. 첫 번재 요소가 같으면 그 다음 요소 비교
# call_order = []
# while waiting:
#     _, _, name = heapq.heappop(waiting)
#     call_order.append(name)
# print(call_order)





# 2
# 4
# 0191
# 1911
# 1119
# 9910
# 5
# 00101
# 99991
# 00001
# 19999
# 11110
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)] 
    #print(arr)

    import heapq
    INF = float('inf')
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    def min_cost(grid, n):
        distance = [[INF] * n for _ in range(n)]
        distance[0][0] = 0 # 시작점은 0
        heap = [(0,0,0)] # 누적거리, 행, 열

        while heap:
            current_dist, row, col = heapq.heappop(heap)
            if distance[row][col] < current_dist:
                continue

            for k in range(4):
                nr = row + dr[k]
                nc = col + dc[k]

                if 0<=nr<n and 0 <= nc <n:
                    new_dist = current_dist + grid[nr][nc]

                    if new_dist < distance[nr][nc]:
                        distance[nr][nc] = new_dist
                        heapq.heappush(heap, (new_dist, nr, nc))
        print(distance)
        return distance[n-1][n-1]

    print(f'#{test_case} {min_cost(arr, N)}') #1 5, #2 9
