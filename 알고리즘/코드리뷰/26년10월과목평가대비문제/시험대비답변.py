# ########################################
# ############ 진수 변환 ###############
# ########################################
# binary_str = '11110110'
# num = int(binary_str, 2) #2진수를 10진수로 변환
# print(num) 
# print(format(num, 'X')) # 16진수
# print(format(num, 'x')) # 16진수
# print(format(num, 'o')) # 8진수
# print(format(num, '04b')) #2진수, 4자리, 빈자리는 0으로

# print(bin(252).replace('0b', '')) # 2진수
# print(hex(252)[2:]) # 16진수
# print(oct(252)) # 8진수

# her_str ='4A'
# result = ''
# for i in range(len(her_str)):
#     hex_to_ten = int(her_str[i], 16)
#     ten_to_bin = format(hex_to_ten, '04b')
#     result += ten_to_bin
# print(f'16진수를 2진수로 변환: {result}') # 01001010




# ########################################
# ############ 부분 집합 만들기 ###############
# ############ 합이 10인 부분 집합 찾기
# ########################################
# # 재귀로 만들기
# arr = list(range(1, 11))
# N = len(arr)

# def subset_recursion(k, input_subset):
#     # 가지치기
#     if sum(input_subset) > 10:
#         return
    
#     # 종료조건
#     if k == N:
#         if sum(input_subset) == 10:
#             print(*input_subset)
#         return

#     # 다음 후보군
#     subset_recursion(k+1, input_subset + [arr[k]])
#     subset_recursion(k+1, input_subset)

# print('재귀')
# subset_recursion(0, [])

# # 백트래킹으로 찾기
# arr = list(range(1, 11))
# N = len(arr)
# # 방문 여부
# included = [False] * N
# def subset_backtracking(k, subset):
#     # 가지치기
#     if sum(subset) > 10:
#         return

#     # 종료 조건
#     if k == N:
#         if sum(subset) == 10:
#             for i in range(N):
#                 if included[i]:
#                     print(arr[i], end = ' ')
#             print()
#         return

#     included[k] = True
#     subset_backtracking(k+1, subset + [arr[k]])
#     included[k] = False
#     subset_backtracking(k+1, subset)

# print('백트래킹')
# subset_backtracking(0, [])




# ########################################
# ############ 2817_부분수열의 합 ###############
# ############ N개의 자연수가 주어졌을 때, 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램을 작성하시오.
# ########################################
# # N은 자연수 개수. K는 합했을 때의 결과
# N, K = 4, 3
# arr = [1, 2, 1, 2]

# def sum_to_K(idx, subset):
#     global cnt

#     # 가지치기
#     if sum(subset) > K:
#         return

#     # 종료 조건
#     if idx == N:
#         if sum(subset) == K:
#             cnt += 1
#         return

#     # 후보군
#     sum_to_K(idx+1, subset + [arr[idx]])
#     sum_to_K(idx+1, subset)

# cnt = 0
# sum_to_K(0, [])
# print(cnt) #4





# ########################################
# ############ 5215_햄버거_다이어트 ###############
# ############ 주어진 제한 칼로리 이하의 조합중에서 가장 맛에 대한 점수가 높은 햄버거의 점수를 출력한다.
# ########################################

# # N은 재료의 수. L은 제한 칼로리
# N, L = 5, 1000
# #맛에 대한 점수 T와 칼로리K
# arr_TK = [[100,200], [300, 500], [250, 300], [500, 1000], [400, 400]]

# def find_best_taste(k, taste, cal):
#     global best_taste
#     # 가지치기
#     if cal > L:
#         return

#     # 종료조건
#     if k == N:
#         best_taste = max(best_taste, taste)
#         return
    
#     # 할당
#     T, K = arr_TK[k]

#     # 후보군 탐색
#     find_best_taste(k+1, taste+T, cal+K)
#     find_best_taste(k+1, taste, cal)

# best_taste = 0
# find_best_taste(0, 0, 0)
# print(best_taste) # 750





# ########################################
# ############ 1486_장훈이의_높은선반 ###############
# ############ 만들 수 있는 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 작은 것을 출력한다.
# ########################################
# N, B = 5, 16
# people = [1, 3, 3, 5, 6]

# def make_top(k, subset):
#     global min_top
#     # 종료 조건
#     if k == N:
#         if sum(subset) >= B:
#             min_top = min(min_top, sum(subset))
#         return

#     # 후보군 탐색
#     make_top(k+1, subset+[people[k]])
#     make_top(k+1, subset)

# min_top = float('inf')
# make_top(0, [])
# ans = abs(min_top - B)
# print(ans) #1





# ########################################
# ############ BFS 구현 ###############
# ############ 모든 정점 경로 출력. 시작 정점은 1
# ########################################
# V, E = 7,8
# edge = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# adj_list = [[] for _ in range(V+1)]
# for i in range(E):
#     node1, node2 = edge[i*2], edge[i*2+1]
#     adj_list[node1].append(node2)
#     adj_list[node2].append(node1)

# visited = [False] * (V+1)
# path = []
# from collections import deque
# def dfs(start_node):
#     queue = deque()
#     queue.append(start_node)
#     visited[start_node] = True
#     while queue:
#         current_node = queue.popleft()
#         path.append(current_node)
#         for next_node in adj_list[current_node]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)

# dfs(1)
# ans = ''.join(map(str, path))
# print(ans) #1234576





# ########################################
# ############ DFS 구현 ###############
# ############ 모든 정점 경로 출력. 시작 정점은 1
# ########################################
# # 스택으로 DFS 구현.
# V, E = 7,8
# edge = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# adj_list = [[] for _ in range(V+1)]
# for i in range(E):
#     node1, node2 = edge[i*2], edge[i*2+1]
#     adj_list[node1].append(node2)
#     adj_list[node2].append(node1)

# visited = [False] * (V+1)
# path = []
# def dfs_stack(start_node):
#     stack = []
#     stack.append(start_node)

#     while stack:
#         current_node = stack.pop()
#         if not visited[current_node]:
#             visited[current_node] = True
#             path.append(current_node)
#         else:
#             continue # 이미 방문한 지점이면 for문을 돌지 말고 continue
#         for next_node in adj_list[current_node]:
#             if not visited[next_node]:
#                 stack.append(next_node)

# for i in range(len(adj_list)):
#     adj_list[i].sort(reverse=True)
# dfs_stack(1)
# ans = ''.join(map(str, path))
# print(f'스택으로 구현: {ans}')



# # 재귀로 DFS구현
# V, E = 7,8
# edge = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# adj_list = [[] for _ in range(V+1)]
# for i in range(E):
#     node1, node2 = edge[i*2], edge[i*2+1]
#     adj_list[node1].append(node2)
#     adj_list[node2].append(node1)

# visited = [False] * (V+1)
# path = []
# def dfs_recursion(start_node):
#     visited[start_node] = True
#     path.append(start_node)

#     for next_node in adj_list[start_node]:
#         if not visited[next_node]:
#             dfs(next_node)
# dfs(1)
# print(f'재귀로 구현: ', end = '')
# print(path)




# ########################################
# ############ 순열 구현 ###############
# ########################################
# def permutation(arr, r):
#     result = []
#     def pick_next(selected, remaining):
#         # 종료 조건
#         if len(selected) == r:
#             result.append(selected)
#             return 

#         for i in range(len(remaining)):
#             pick = remaining[i]
#             next_remaining = remaining[:i] + remaining[i+1:]
#             pick_next(selected + [pick], next_remaining)

#     pick_next([], arr)
#     return result

# print('순열')
# ans = permutation([1,2,3,4], 2)
# print(*ans)

# # itertools 사용
# import itertools
# a = list(itertools.permutations([1,2,3,4], 2))
# print(*a)

# ########################################
# ############ 조합 구현 ###############
# ########################################
# def combination(arr, r):
#     """
#     arr은 숫자 선택지
#     r은 선택할 개수
#     """
#     # 종료 조건
#     if r == 0 :
#         return [[]]

#     result = []
#     for i in range(len(arr)):
#         elem = arr[i]
#         next_arr = arr[i+1:]
#         for next_comb in combination(next_arr, r-1):
#             result.append([elem] + next_comb)

#     return result 

# print('조합')
# ans = combination([1,2,3,4], 2)
# print(*ans)

# # itertools 사용
# import itertools
# a = list(itertools.combinations([1,2,3,4], 2))
# print(*a)


# ########################################
# ########### 조건 명제의 진리표 ###########
# ########################################
# 명제: 참이나 거짓을 알 수 있는 식이나 문장
# 조건 명제: 명제 p가 조건(원인), q가 결론(결과)으로 제시되는 명제. p -> q
# 쌍방조건명제: p <-> q. p와 q 둘 다 참이거나 둘 다 거짓이어야 p <-> q 가 참.
# 조건명제의 역, 이, 대우
    # 주어진 명제: p -> q
    # 역: q -> p
    # 이: ~p -> ~q
    # 대우: ~q -> ~p



# ########################################
# ########### MST의 정의와 알고리즘 ###########
# ########################################
# MST(Minimum Spanning Tree)
# 가중치가 있는 / 무방향 연결 그래프에서 / 모든 정점을 / 사이클 없이 연결하는 / 신장 트리 중 / 간선 가중치의 합이 최소인 트리.
# 정점이 V개면 간선은 V-1개. 간선이 그보다 많으면 사이클이 있고 그보다 적으면 끊어진 지점이 있기 때문.

# 크루스칼(Kruskal) 알고리즘
# 간선 중심의 그리디 알고리즘. 모든 간선을 가중치 오름차순으로 정렬한 뒤 / 가장 작은 간선부터 선택하되 / 사이클을 만드는 간선은 건너 뛴다.
# 사이클 여부는 Union-Find(서로서 집합)로 판별 / 선택한 간선이 V-1개가 되면 종료.
# 간선 수가 적은 희소 그래프에 유리.

# 프림(Prim) 알고리즘
# 정점 중심의 그리디 알고리즘. 임의의 시작 정점에서 출발해 / 현태 트리에 포함된 정점과 아직 포함되지 않은 정점을 잇는 간선 중 가중치가 가장 작은 것을 골라 트리를 하나씩 확장.
# 우선 순위 큐(heap)로 최소 간선을 효율적으로 고를 수 있음.
# 간선이 많은 밀집 그래프에 유리.


# 크루스칼 알고리즘
arr = [i for i in range(5)] # [0,1,2,3,4]
V,E = 4, 5 # 정점, 간선 개수
lst = [(0,1,1), (1,2,2), (0,2,3), (2,3,4), (1,3,5)] # 간선 정보 # (시작, 도착, 비용)
lst.sort(key = lambda x:x[2]) # 비용을 기준으로 sort

total = 0 # 비용 더하기
cnt = 0 # 연결된 간선 개수

def findboss(m):
    global arr
    if arr[m]==m:
        return m
    ret=findboss(arr[m])
    arr[m] = ret # 경로 저장
    return ret

def union(a,b,i): # 시작점, 도착점, 비용
    global total, cnt
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return # 두 보스가 같으면 넘어감
    total +=lst[i][2] # 비용을 기준으로 sort했으니까
    cnt +=1
    arr[fb]=fa

for i in range(V):
    if cnt == V-1: # 정점의 개수 -1개만큼 합 구하기
        print(total) # 합 출력하고 종료
        break
    union(lst[i][0],lst[i][1],i) # (시작점, 도착점, 비용)

print(total) # 7



# 프림 알고리즘
import heapq
V = 4
E = 5

# arr = [[] for _ in range(n)]
# # 무방향 그래프이므로 양뱡향 저장
# for _ in range(m):
#     start, end, cost = map(int, input().split())
#     arr[start].append((cost, end)) 
#     arr[end].append((cost, start))

adj_list = [[(1, 1), (3, 2)], [(1, 0), (2, 2), (5, 3)], [(2, 1), (3, 0), (4, 3)], [(4, 2), (5, 1)]]

used = [0] * V # 내가 선택한 정점인지 체크하는 리스트
heap = []

# (비용, 정점)
heapq.heappush(heap, (0,0)) # (비용, 시작 정점) 넣고 시작
total = 0 # 총 비용을 합치기
cnt = 0 # 연결한 간선의 개수

while heap:
    cost, now = heapq.heappop(heap)

    # 이미 MST에 포함된 정점이면 무시
    if used[now] == 1:
        continue

    # MST에 포함되 않은 정점이라면
    used[now] = 1 # 방문체크해서 MST에 포함
    total += cost # 비용의 합
    cnt += 1 # 연결된 간선의 개수 1증가

    # 모든 정점을 선택했다면 종료
    if cnt == V:
        break

    # 현재 정점과 연결된 간선들을 우선순위 큐에 추가
    for next_cost, next_node in adj_list[now]:
        if used[next_node] == 0:
            heapq.heappush(heap, (next_cost, next_node))

print(total) # 7
