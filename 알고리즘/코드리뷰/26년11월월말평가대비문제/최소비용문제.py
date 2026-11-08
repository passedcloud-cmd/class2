# 그래프 최소 비용 문제
# 유형 1. 최소 신장 트리(MST):
# 모든 정점을 연결하는 간선들의 비용 합을 최소로 만들기 - "모든 마을을 잇는 도로를 가장 싸게 깔려면?" 

# 프림: 한 정점에서 시작해서 지금 트리에 붙일 수 있는 가장 저렴한 간선을 하나씩 추가. 아무데서나 시작. 무방향 그래프.
# 우선순위 큐(힙) 사용.
# 시간 복잡도: O(ElogV). 간선이 많은 밀집 그래프는 프림이 유리

# 크루스칼: 전체 간선을 저렴한 비용 순으로 정렬하고, 저렴한 간선부터 연결. 사이클이 생기는 간선은 건너뛴다. 출발점 없음. 무방향 그래프.
# 정렬 + 서로소 집합(Union-Find) 사용
# 시간 복잡도: O(ElogE). 간선이 적은 희소 그래프에서 유리




# 유형 2: 최단 경로
# 특정 정점 사이의 경로 비용을 최소로 만들기 - "우리 집에서 학교까지 가장 싸게 가려면?" 

# 다익스트라: 한 정점에서 모든 정점까지 구함=한 정점에서 각 정점까지 가는 최단거리. 음수 가중치 불가. 우선순위 큐(힙) 사용.
# 가장 가까운 정점부터 확정해 나감.
# 시간 복잡도: O(E logV) (프림과 같음)

# 벨만-포드: 한 정점에서 모든 정점까지 구함. 음수 가중치 가능, 음수 사이클 판별 가능. 모든 간선을 V-1번 반복 완화
# 시간 복잡도: O(VE)

# 플로이드-워셜: 모든 정점 쌍 사이를 구함. 음수 가중치 가능, 음수 사이클은 없어야 함. 3중 for문 (DP)
# 시간 복잡도: O(V³)




# 한눈에 고르는 기준
# 1. 모든 정점을 연결하는 최소 비용이면 => MST (크루스칼 / 프림)
# 2. 출발점이 하나이고 가중치가 0 이상이면 => 다익스트라
# 3. 음수 가중치가 있거나 음수 사이클을 찾아야 하면 => 벨만-포드
# 4. 모든 쌍의 최단 거리가 필요하고 정점이 수백 개 이하이면 => 플로이드-워셜




# priority queue 우선순위 큐
# 우선순위가 가장 높은 값(원소)부터 나오는 자료구조
# 첫 번째 원소만 보면 됨. heap구조이기 때문

# # 우선 순위 큐
# import heapq
# arr = []
# heapq.heappush(arr, 13) # min heap
# heapq.heappush(arr, 5)
# heapq.heappush(arr, 17)
# heapq.heappush(arr, 9)
# print(arr) # [5, 9, 17, 13] -> 다른 요소는 몰라도 첫 번째는 제일 작은 값이 들어있음 

# print(heapq.heappop(arr)) # 5 # 우선순위가 높은 것을 pop
# print(heapq.heappop(arr)) # 9




#prim
import heapq
n = 4 # 정점 개수
m = 5 # 간선 개수
# 0 1 1
# 1 2 2
# 0 2 3
# 2 3 4
# 1 3 5

# # 인근 간선 리스트 만들기
# arr = [[] for _ in range(n)] 
# # 무방향 그래프이므로 양뱡향 저장
# for _ in range(m):
#     start, end, cost = map(int, input().split())
#     arr[start].append((cost, end)) 
#     arr[end].append((cost, start))
# # print(arr)  # 확인용 출력

# used = [0] * n # 내가 선택한 정점인지 체크
# heap = []

# # (비용, 정점)
# heapq.heappush(heap, (0,0)) # (비용, 시작정점)
# total = 0 # 총 비용을 합치기
# cnt = 0 # 연결한 간선의 개수

# while heap:
#     cost, now = heapq.heappop(heap)

#     # 이미 MST에 포함된 정정이면 무시
#     if used[now] == 1:
#         continue

#     # MST에 정점 포함
#     used[now] = 1 # 방문체크 
#     total += cost # 비용의 합
#     cnt += 1 # 연결된 간선의 개수 1증가

#     # 모든 정점을 선택했다면 종료
#     if cnt == n:
#         break

#     # 현재 정점과 연결된 간선들을 우선순위 큐에 추가
#     for next_cost, next_node in arr[now]:
#         if used[next_node] == 0: # 다음 노드에 방문한 적 없다면.
#             heapq.heappush(heap, (next_cost, next_node))

# print(total) #7








# 크루스칼
arr = [i for i in range(5)]
n,m = 4, 5 # 정점, 간선 개수
lst = [[0, 1, 1],[1, 2, 2],[0, 2, 3],[2, 3, 4],[1, 3, 5]] # 간선 정보 # (시작, 도착, 비용)


lst.sort(key = lambda x:x[2]) # 비용을 기준으로 sort
# print(lst)
total = 0 # 비용 더하기
cnt = 0 # 연결된 간선 개수

def findboss(m):
    global arr
    if arr[m]==m:
        return m
    ret=findboss(arr[m])
    arr[m] = ret
    return ret

def union(a,b,i): # 시작점, 도착점, 비용 
    global total, cnt
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return
    total +=lst[i][2] # 비용을 기준으로 sort했으니까
    cnt +=1
    arr[fb]=fa

for i in range(m):
    if cnt ==n-1: # 정점의 개수 -1개만큼 합 구하기
        print(f'크루스칼 합: {total}') # 합 출력하고 종료
        break
    union(lst[i][0],lst[i][1],i) # (시작점, 도착점, 비용)

# 출력은 7