# 최소 비용 신장 트리 - minimum spanning tree
    # prim 알고리즘과 kruskal 알고리즘이 MST를 풀 수 있는 알고리즘
# 최단거리 - Dijkstra 알고리즘

# priority queue 우선순위 큐
# 우선순위가 가장 높은 값(원소)부터 나오는 자료구조
# 첫 번째 원소만 보면 됨. heap구조이기 때문

# heap : 우선순위가 높은 것부터 출력, 삭제하는 자료 구조
# 완벽한 이진트리의 형태를 유지. nlog N
# max heap - 큰 갓이 우선순위
# min heap - 작은 값이 우선순위

# # 우선 순위 큐
# import heapq
# arr = []
# heapq.heappush(arr, 13) # min heap
# heapq.heappush(arr, 5)
# heapq.heappush(arr, 17)
# heapq.heappush(arr, 9)
# print(arr)

# print(heapq.heappop(arr)) # 5# 우선순위가 높은 것을 pop
# print(heapq.heappop(arr)) # 9

# for i in range(len(arr)):
#     print(heapq.heappop(arr), end= ' ')

# while arr:
#     node = heapq.heappop(arr)
#     print(node, end=' ')



# import heapq
# arr = [3, 234,23,12,31]
# heap = []
# for i in range(len(arr)):
#     heapq.heappush(heap, -arr[i]) # max 힙
# for i in range(len(arr)):
#     print(-heapq.heappop(heap), end = ' ')
# print()

# # 아래가 더 빠름 
# import heapq
# arr = [3,234,23,12,31]
# arr = list(map(lambda x: -x, arr)) # arr 배열의 모든 원소에 -를 붙인 후 arr에 재할당
# heapq.heapify(arr) # min힙으로 배열
# for i in range(len(arr)):
#     print(-heapq.heappop(arr), end=' ') # arr의 원소들이 음수이기 때문에 다시 -를 붙여서 양수로 만듦


#prim 알고리즘




#prim
import heapq
n = int(input())
m = int(input())

# 4
# 5
# 0 1 1
# 1 2 2
# 0 2 3
# 2 3 4
# 1 3 5
# 출력은 7
arr = [[] for _ in range(n)]
# 무방향 그래프이므로 양뱡향 저장
for _ in range(m):
    start, end, cost = map(int, input().split())
    arr[start].append((cost, end)) 
    arr[end].append((cost, start))

print(arr)    

used = [0] * n # 내가 선택한 정점인지 체크
heap = []

# (비용, 정점)
heapq.heappush(heap, (0,0)) # (비용, 시작정점)
total = 0 # 총 비용을 합치기
cnt = 0 # 연결한 간선의 개수

while heap:
    cost, now = heapq.heappop(heap)

    # 이미 MST에 포함된 정정이면 무시
    if used[now] == 1:
        continue

    # MST에 정점 포함
    used[now] = 1 # 방문체크 
    total += cost # 비용의 합
    cnt += 1 # 연결된 간선의 개수 1증가

    # 모든 정점을 선택했다면 종료
    if cnt ==n:
        break

    # 현재 정점과 연결된 간선들을 우선순위 큐에 추가
    for next_cost, next_node in arr[now]:
        if used[next_node] == 0:
            heapq.heappush(heap, (next_cost, next_node))

print(total)





# prim - 정점과 연결된 간선의 비용 기준. 간선이 정점의 제곱만큼 많으면 prim이 더 효율적일 수 있음.
# kruskal - 간선 비용 기준. 간선이 많지 않을 때 사용하면 좋음.  

# kruskal 알고리즘
# 1. 선택할 간선의 개수 = n-1개
# 2. 내가 선택한 간선에는 cycle이 존재하면 안된다 -> union find로 확인. 연결 후 간선의 가중치를 더함
# 최소 비용 - 간선 선택 시 비용이 가장 작은 것 우선
    # 1. 그래서 가중치 기준 오른차순 정렬 -> 비용이 가장 적게 드는 간선부터 선택
    # 2. union-find로 cycle 여부 체크하면서 간선 선택(cycle 발생할 것 같으면 선택 x)
    # 3. 선택된 가중치를 다 더하는데.... 정점-1개의 간선 선택


# # 크루스칼
# arr = [i for i in range(5)]
# n,m = map(int, input().split()) # 정점, 간선 개수
# lst = [list(map(int,input().split())) for _ in range(m)] # 간선 정보 # (시작, 도착, 비용)
# # 4 5
# # 0 1 1
# # 1 2 2
# # 0 2 3
# # 2 3 4
# # 1 3 5
# # 출력은 7
# lst.sort(key = lambda x:x[2]) # 비용을 기준으로 sort
# # print(lst)
# total = 0 # 비용 더하기
# cnt = 0 # 연결된 간선 개수

# def findboss(m):
#     global arr
#     if arr[m]==m:
#         return m
#     ret=findboss(arr[m])
#     arr[m] = ret
#     return ret

# def union(a,b,i): # 시작점, 도착점, 비용                                                                                                                                                                                                                   
#     global total, cnt
#     fa, fb = findboss(a), findboss(b)
#     if fa == fb:
#         return
#     total +=lst[i][2] # 비용을 기준으로 sort했으니까
#     cnt +=1
#     arr[fb]=fa

# for i in range(m):
#     if cnt ==n-1: # 정점의 개수 -1개만큼 합 구하기
#         print(total) # 합 출력하고 종료
#         break
#     union(lst[i][0],lst[i][1],i) # (시작점, 도착점, 비용)




# MST - 최소신장트리(섬다리 연결) 

# 최소비용, 최단거리 찾기. 시작점 -> 도착점. 
# 다익스트라 조건 1. 시작점(출발)이 정해진다2. 가중치가 양수

# 모든 정점(시작점)에서 다른 모든 정점(도착점)까지 아는 방법은 Floyd warshall(시간 복잡도가 큼)
# 음의 가중치가 있다면 Bellman Ford 알고리즘으로 풂. 다만 음의 사이클이 없어야 함.

# 다익스트라
# 시작 정점에서 거리가 최소인 정점을 선택하면서 최단거리를 찾음
# 탐욕 기법을 사용함
# MST의 Prim 알고리즘과 유사함

# 시작점 -> 경유지 -> 도착점 : 우선순위 q
