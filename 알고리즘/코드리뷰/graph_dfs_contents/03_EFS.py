import sys
sys.stdin = open('03_EFS.txt')

V, E = map(int, input().split())
edge_input = list(map(int, input().split()))

# 인접 리스트 + 스택으로 구현
adj_list = [[] for _ in range(V+1)]

for i in range(E):
    node1, node2 = edge_input[i*2], edge_input[i*2 + 1]
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

# 인접한 노드를 내림차순으로 정렬해야 pop으로 노드 순회 시 숫자가 작은 노드 먼저 방문
for i in range(1, V+1):
    adj_list[i].sort(reverse=True)

# 인접 리스트 확인용 출력 print(adj_list)

visited = [False] * (V + 1)
path = []
stack = []

def adj_list_stack_pop(start_node):
    # 시작점 stack에 넣기
    stack.append(start_node)


    # stack이 빌 때까지 반복
    while stack:
        # 맨 위에 있는 값이 현재 node
        current_node = stack.pop()
        # 만약 현재 노드를 방문한 적 없다면
        if not visited[current_node]:
            # 방문 기록
            visited[current_node] = True
            # 출력 예정에 추가
            path.append(current_node)
            # 인근 노드로 이동
            for next_node in adj_list[current_node]:
                if not visited[next_node]:
                    stack.append(next_node)
                # 방문 안 한 노드가 없으면 stack에 있는 값 전부 pop해버림
                # stack 진행 상황 확인용 출력 print(stack)
                

adj_list_stack_pop(1)
print(''.join(map(str, path)))


#7 8
#1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
#1246573