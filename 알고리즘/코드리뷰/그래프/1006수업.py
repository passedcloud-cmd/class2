# # DFS (인접 행렬) = 가능한 모든 정점 1번씩 탐색
# name = "BACD"
# arr = [
#     [0,0,1,1],
#     [1,0,1,0],
#     [1,0,0,1],
#     [0,0,0,0]]
# used = [0]*4 # 정점의 개수만큼

# def dfs(now): 
#     print(name[now], end= ' ')
#     for i in range(4):
#         if arr[now][i] == 1 and used[i] == 0:
#             used[i]=1
#             dfs(i)
        
# used[1] = 1 # 탐색 시작 인덱스에 1 중복체크
# dfs(1) # 탐색 시작 인덱스







# DFS (인접 리스트)= 한 정점에서 다른 정점까지 도착할 수 있는 방법이 몇 가지?
# 입력
# 4 6
# 0 2
# 0 3
# 1 0 
# 1 2 
# 2 0
# 2 3 

name = "BACD"
n, m = map(int, input().split()) # 정점과 간선 정보의 개수
arr = [[] for _ in range(n)]
for _ in range(m):
    start, end = map(int,input().split())
    arr[start].append(end)
    
used = [0]*n
cnt = 0

def dfs(now):
    global cnt
    if now == 3: # if name[now] == 'D':
        cnt+=1

    for i in arr[now]:
        if used[i] ==0:
            used[i] =1
            dfs(i)
            used[i]=0 #경로 탐색할 거면 used를 0으로 다시 바꿔줌

# A에서 D까지
used[1] = 1
dfs(1)
print(cnt) #4






# BFS 너비우선 탐색(모든 정점을 한번씩 탐색)
# 4 6
# 0 1
# 0 2
# 1 2
# 1 3
# 2 1
# 2 3

from collections import deque
n,m = map(int,input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)

q=deque()
used = [0] * n
q.append(0) # 시작점 큐에 넣기
used[0]=1 # 시작점 방문체크
name="ABCD"
while q:
    now = q.popleft() # 큐에 있는 거 빼기
    print(name[now], end=' ')
    for i in arr[now]: # 이동 가능한 것 탐색
        if used[i] ==0: # 방문여부 확인
            used[i]=1 # 방문체크
            q.append(i) # 큐에 넣기

# BFS에서 경로탐색을 할 땐 큐 안에 used 배열을 넣어주기






# # union-find 자료구조
# # 각각의 독립된 data를 그룹화해서 관리 -> 사이클 확인도 가능

# # union이라는 함수를 임의로 만듦
# # union(0,1) -> 0이 속한 그룹과 1이 속한 그룹을 합침

# # arr = [i for i in range(6)] #[0, 1, 2, 3, 4, 5]
# # print(arr)
# arr=[0, 1, 2, 3, 4, 5]

# def findboss(member):
#     if arr[member] == member: # 자기 자신이 보스라면 그 그룹의 보스 찾음
#         return member
#     ret = findboss(arr[member]) # 자기 자신이 보스가 아니라면 arr배열의 값을 가지고 보스 찾기
#     arr[member] = ret # !경로 단축 코드!
#     return ret

# def union(a,b):
#     fa = findboss(a)
#     fb = findboss(b)
#     if fa==fb: # 두 보스가 같으면 이미 같은 그룹
#         return

#     arr[fb]=fa # 보스가 다르면 a의 보스가 통합 장

# union(0,1)
# union(3,4)
# union(1,4)
# union(1,3)
# union(5,4)

# y,x = map(int, input().split()) # 숫자 2개 입력 후 같은 그룹인지 출력
# if findboss(y) == findboss(x):
#     print("같그룹")
# else:
#     print("다른 그룹")

# print(arr)


# # 최적화? rank 추가
# # 랭크가 같은 트리를 더하면 랭크 크기 1 증가하여 합치기
# # 랭크가 다르면 랭크가 작은 것을 랭크가 큰 것으로 합치기
# # 깊이가 작은 트리가 큰 트리로 들어감
# arr=[0, 1, 2, 3, 4, 5]
# rank = [0]*6

# def findboss(member):
#     if arr[member] == member: # 자기 자신이 보스라면 그 그룹의 보스 찾음
#         return member
#     ret = findboss(arr[member]) # 자기 자신이 보스가 아니라면 arr배열의 값을 가지고 보스 찾기
#     arr[member] = ret # !경로 단축 코드!
#     return ret

# def union(a,b):
#     fa = findboss(a)
#     fb = findboss(b)
#     if fa==fb: # 두 보스가 같으면 이미 같은 그룹
#         return

#     # arr[fb]=fa # 보스가 다르면 a의 보스가 통합 장
#     if rank[a] == rank[b]:
#         rank[a]+=1
#         arr[fb]=fa
#     elif rank[a]>rank[b]:
#         arr[fb] = fa
#     else:
#         arr[fa]= fb

# union(0,1)
# union(3,4)
# union(1,4)
# union(1,3)
# union(5,4)

# y,x = map(int, input().split()) # 숫자 2개 입력 후 같은 그룹인지 출력
# if findboss(y) == findboss(x):
#     print("같그룹")
# else:
#     print("다른 그룹")
