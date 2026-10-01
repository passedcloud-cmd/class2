# 3단계: 스택 DFS - Pop 시점 방문 처리 vs Push 시점 방문 처리
#
# 학습 목표
#   - 스택용 인접 리스트를 왜 내림차순으로 정렬하는지 설명할 수 있다.
#   - 방문 처리를 pop 할 때 하느냐 push 할 때 하느냐에 따라 결과가 왜 달라지는지 설명할 수 있다.
#   - 재귀 DFS와 같은 순서를 내는 쪽이 어느 방식인지 안다.
#
# 시간 복잡도: O(V + E)
# 공간 복잡도: Pop 방식 O(V + E) (같은 노드가 중복 적재될 수 있음) / Push 방식 O(V)

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '03_input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    node1 = data[i * 2]
    node2 = data[i * 2 + 1]

    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

# [실습 1] 정렬 방향 정하기
#   스택은 나중에 넣은 것을 먼저 꺼냅니다(LIFO).
#   '작은 번호부터 방문' 하려면 스택에는 어떤 순서로 쌓아야 할까요?
for i in range(1, V + 1):
    # 인접 리스트 정보를 내림차순으로 변경
    # 스택에 다음 방문지를 넣을 때 큰 번호 노드를 먼저 넣어야 하기 때문
    # 먼저 넣은 걸 나중에 꺼내니까.
    adj_list[i].sort(reverse=True)  # TODO: 

print('인접 리스트(스택용):')
for i in range(1, V + 1):
    print(f'  {i}: {adj_list[i]}')
print()


# ------------------------------------------------------------
# [실습 2] Pop 시점 방문 처리  (재귀 DFS와 같은 순서가 나와야 합니다)
# ------------------------------------------------------------
def dfs_stack_pop_style(start):
    """
    스택에서 '꺼낸 뒤에' 방문 여부를 확정 짓는다.
    """
    # 방문 기록지 준비
    visited = [False] * (V + 1)
    # 일단 시작 노드는 스택에 넣고 시작
    stack = [start]
    # 최종 누적될 경로
    path = []

    # 더 이상 스택에 넣을 노드가 없을 때까지 반복
    while stack:
        # 2-1. 스택에서 꺼내기
        # TODO: 이 줄은 '맨 앞'에서 꺼냅니다. 스택은 어디서 꺼내야 할까요?
        # 스택은 top에서 꺼낸다.
        current = stack.pop() 

        # 2-2. 꺼낸 시점에 아직 방문 전이라면, 그때 방문 처리합니다.
        if not visited[current]:
            # 방문 처리하고 path 에 기록하세요.
            # 이 부분을 비워 둔 채 2-3만 채우면 무한 루프에 빠집니다. 여기를 먼저 채우세요.
            # TODO
            visited[current] = True # 방문 경로에 넣고
            path.append[current] # 최종 경로에 추가

            # 현재 노드와 인접한 노드가 누구인지 탐색
            for next_node in adj_list[current]:
                if not visited[next_node]:
                    # 2-3. 아직 방문하지 않은 이웃을 스택에 넣으세요.
                    # TODO
                    stack.append(next_node)

    return path


# ------------------------------------------------------------
# [실습 3] Push 시점 방문 처리  (BFS의 구현 방식과 같습니다)
# ------------------------------------------------------------
def dfs_stack_push_style(start):
    visited = [False] * (V + 1)
    visited[start] = True
    stack = [start]
    path = []

    while stack:
        current = stack.pop()
        path.append(current)

        for next_node in adj_list[current]:
            if not visited[next_node]:
                # 넣기 '직전에' 방문을 예약하고 스택에 넣으세요.
                # 이 순서 때문에 한 노드는 스택에 최대 한 번만 들어갑니다.
                # TODO
                visited[next_node] = True
                stack.append(next_node) # 순서가 뒤바뀌는 순간이 올 수 있음. 탐색으로서 틀린 건 아님. 다만 정답을서는 틀릴 수도

    return path


path_pop = dfs_stack_pop_style(1)
path_push = dfs_stack_push_style(1)

print(f'Pop  시점 방문 처리: {"".join(map(str, path_pop))}   <- 정답 1246573')
print(f'Push 시점 방문 처리: {"".join(map(str, path_push))}   <- 정답 1246753')
print('=> 같은 그래프, 같은 정렬인데 결과가 다릅니다. 왜일까요?')
print()


# --- 동작 과정 시각화 (완성되어 있습니다) ---
# 두 방식의 스택 상태를 단계별로 찍습니다. 실습을 마친 뒤 결과를 대조해 보세요.
def trace(style):
    visited = [False] * (V + 1)
    stack = [1]
    path = []

    if style == 'push':
        visited[1] = True

    print(f'--- {style.capitalize()} 시점 방문 처리 ---')
    while stack:
        current = stack.pop()

        if style == 'pop' and visited[current]:
            print(f'  pop {current} -> 이미 방문. 건너뜀      | 스택 {stack}')
            continue

        visited[current] = True
        path.append(current)

        pushed = []
        for next_node in adj_list[current]:
            if not visited[next_node]:
                if style == 'push':
                    visited[next_node] = True
                stack.append(next_node)
                pushed.append(next_node)

        mark = '   <=== 여기서 갈라진다' if current == 6 else ''
        print(
            f'  pop {current} -> 방문. push {str(pushed):9s} | '
            f'스택 {str(stack):15s} | 경로 {"".join(map(str, path))}{mark}'
        )

    print(f'  결과: {"".join(map(str, path))}')
    print()


print('=== 스택 상태 추적 ===')
trace('pop')
trace('push')

print('=== 왜 갈라지는가 ===')
print('노드 6의 인접 노드는 내림차순으로 [7, 5, 4] 입니다.')
print()
print('Pop  방식: 6을 처리하는 시점에 5는 아직 "방문 처리 전" 입니다.')
print('           (2번에서 스택에 넣기만 했을 뿐입니다)')
print('           그래서 5가 스택에 한 번 더 쌓여 맨 위에 올라옵니다 -> 5를 먼저 방문')
print()
print('Push 방식: 5는 2번을 처리할 때 이미 "예약(visited=True)" 되었습니다.')
print('           그래서 다시 쌓이지 않고, 맨 위에는 7이 남습니다 -> 7을 먼저 방문')
print()
print('핵심은 "같은 노드의 중복 적재를 허용하느냐" 입니다.')
print('  Pop  방식 -> 허용. 가장 나중에 쌓인 위치가 순서를 정합니다. (재귀와 동일)')
print('  Push 방식 -> 불허. 처음 예약된 위치가 방문 순서를 정합니다.')
