from collections import deque
n,m = map(int,input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)

q= deque()
visited = [0] * n
q.append(0)
visited[0] = 1
name = "ABCD"
while q:
    current = q.popleft()
    print(name[current], end = ' ')
    for next in arr[current]:
        if visited[next] ==0:
            visited[next] =1
            q.append(next)





# import sys
# sys.stdin = open('5248-그룹나누기.txt')

# T = int(input())
# for test_case in range(1, T+1):
#     # N은 학생 수, M은 신청서 수 
#     N, M = map(int, input().split())
#     applyer = list(map(int, input().split()))

#     groups = [i for i in range(N+1)]

#     def findboss(member):
#         if groups[member] == member:
#             return member
#         ret = findboss(groups[member])
#         groups[member] = ret
#         return ret

#     def union(a,b):
#         fa = findboss(a)
#         fb = findboss(b)
#         if fa == fb:
#             return
#         groups[fb] = fa

#     for i in range(M):
#         union(applyer[i*2], applyer[i*2+1])

#     for i in range(1,N+1):
#         findboss(i)
    
#     # 확인용 출력
#     print(groups)

#     make_set = set()
#     for i in range(1, N+1):
#         make_set.add(groups[i]) 

#     print(len(make_set))

# 오답노트
# set에 요소를 추가할 땐 append가 아니라 add임을 주의!!!!





# import sys
# sys.stdin = open('5248-그룹나누기.txt')

# T = int(input())
# for test_case in range(1, T+1):
#     # N은 학생 수, M은 신청서 수 
#     N, M = map(int, input().split())
#     applyer = list(map(int, input().split()))

#     # 인접 리스트 만들기
#     adj_list = [[] for i in range(N+1)]
#     for i in range(M):
#         node1, node2 = applyer[i*2], applyer[i*2+1]
#         adj_list[node1].append(node2)
#         adj_list[node2].append(node1)

#     # BFS 만들기
#     from collections import deque
#     def BFS(start_node, adj_list, visited):
#         queue = deque()
#         # 먼저 queue에 start_node를 넣고 방문했다고 체크
#         queue.append(start_node)
#         visited[start_node] = True

#         # queue가 빌 때까지 반복
#         while queue:
#             current_node = queue.popleft()
#             # 인접리스트를 참고하여 인접한 노드들을 모두 방문 시도
#             for next_node in adj_list[current_node]:
#                 # next_node에 방문한 적이 없다면
#                 if not visited[next_node]:
#                     # 방문할 거니까 방문 체크
#                     visited[next_node] = True
#                     # queue에 next_node 추가
#                     queue.append(next_node)

#     # 방문 체크 리스트 만들기
#     visited = [False] * (N+1)

#     # 그룹의 개수는 0으로 시작
#     cnt = 0
#     # 모든 학생들을 돌면서 그룹 체크
#     for i in range(1, N+1):
#         # 만약 i번째 학생을 방문하지 않았다면 = i번째 학생이 속한 그룹을 방문하지 않았다면
#         if not visited[i]:
#             # 카운트 1 적립
#             cnt += 1
#             # 해당 학생과 같은 그룹인 학생은 모두 방문 처리
#             BFS(i, adj_list, visited)

#     print(f'#{test_case} {cnt}')
    