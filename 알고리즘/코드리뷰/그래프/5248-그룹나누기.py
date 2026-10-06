#서로소 집합
import sys
sys.stdin = open('5248-그룹나누기.txt')

T = int(input())
for test_case in range(1, T+1):
    # N은 학생 수, M은 신청서 수 
    N, M = map(int, input().split())

    # 그룹을 합치기 전, 각 학생들이 조장인 1인 조
    # 출석번호가 1번부터 시작하므로 출석번호와 인덱스 번호를 맞추기 위해 0번 인덱스는 더미로 둔다.
    group = [i for i in range(N+1)]

    # 그룹의 보스를 찾는 함수 만들기
    def findboss(member):
        # 그룹의 보스가 자기 자신인 경우
        if group[member] == member:
            return member
        # 그룹의 보스가 자신이 아닌 경우
        ret = findboss(group[member])
        group[member] = ret # 경로 추적. 해당 member의 보스를 기록함.
        return ret

    # 두 그룹을 합치는 함수 만들기
    def union(a, b):
        fa = findboss(a)
        fb = findboss(b)
        # 두 그룹의 보스가 같으면 그냥 넘어가기
        if fa == fb:
            return
        # 두 그룹의 보스가 다르면 a의 보스가 b의 보스가 됨
        group[fb] = fa

    # 신청서 묶음
    apply_list = list(map(int, input().split()))
    # 신청서 묶음 리스트에서 2개씩 묶음이 신청서 1개임
    # [1, 2, 3, 4] 이면 신청서가 union(1,2)와 union(3,4)로 2개인 것
    for i in range(M):
        union(apply_list[i*2], apply_list[i*2+1])

    # 모든 요소에 findboss 함수를 가해서 각 member의 최종 보스를 경신함
    for i in range(1,N+1):
        findboss(i)

    # 중복되는 값들을 제거하기 위해 set를 만듦
    make_a_set = set()
    # set에 각 학상들의 최종보스를 추가
    for i in range(1,N+1):
        make_a_set.add(group[i])

    # make_a_set의 길이가 최종보스들의 수 = 그룹의 수
    print(f'#{test_case} {len(make_a_set)}')
    





# BFS
import sys
sys.stdin = open('5248-그룹나누기.txt')

T = int(input())
for test_case in range(1, T+1):
    # N은 학생 수, M은 신청서 수 
    N, M = map(int, input().split())
    group = list(map(int, input().split()))

    from collections import deque
    def bfs(start_node, adj_list, visited):
        """
        start_node와 연결된 노드는 모두 방문 처리
        """
        queue = deque()
        queue.append(start_node)
        visited[start_node] = True

        while queue:
            current_node = queue.popleft()
            for next_node in adj_list[current_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)


    # 인접 리스트 만들기
    adj_list = [[] for _ in range(N+1)]
    for i in range(M):
        node1, node2 = group[i*2], group[i*2+1]
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    visited = [False] * (N+1)
    group_count = 0

    for i in range(1, N+1):
        if not visited[i]:
            group_count += 1
            bfs(i,adj_list, visited)

    print(f'#{test_case} {group_count}')

# 입력
# 3
# 5 2
# 1 2 3 4
# 5 3
# 1 2 2 3 4 5
# 7 4
# 2 3 4 5 4 6 7 4
# 출력
# #1 3
# #2 2
# #3 3