# import sys
# sys.stdin = open('5174-subtree.txt')

# T = int(input())
# for test_case in range(1, T+1):
#     # 간선의 개수 E, 서브 트리의 노드 N
#     E, N = map(int, input().split())
#     V = E+1
#     edge = list(map(int, input().split()))

#     child1 = [0] * (V+1)
#     child2 = [0] * (V+1)

#     for i in range(E):
#         parent = edge[i*2]
#         child = edge[i*2+1]

#         if child1[parent] == 0:
#             child1[parent] = child
#         else:
#             child2[parent] = child

#     # 자식 노드 확인 출력
#     # print(f'child1:{child1}')
#     # print(f'child2:{child2}')

#     cnt = 0
#     # 전위순회
#     def preorder(node):
#         global cnt
#         if node != 0:
#             # print(node, end = ' ')
#             cnt +=1
#             preorder(child1[node])
#             preorder(child2[node])
#         return cnt
    
#     preorder(N)
#     print(f'#{test_case} {cnt}')





import sys
sys.stdin = open('5174-subtree.txt')

def postorder(T):
    if T == 0:
        return 0
    l = postorder(left[T])
    r = postorder(right[T])
    return l + r + 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    V = E + 1   # 정점 개수 = 간선 수 + 1

    left = [0] * (V + 1)
    right = [0] * (V + 1)
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    cnt = postorder(N)
    print(f'#{tc} {cnt}')










# def pre_order(T):
#     global cnt
#     if T:
#         cnt += 1
#         pre_order(left[T])
#         pre_order(right[T])
#
# def f(T):
#     if T == 0: # 없는 정점이면
#         return 0 # 방문한 개수는 0개
#     # l은 왼쪽 서브트리의 정점 개수
#     l = f(left[T])
#     r = f(right[T])
#     return l + r + 1
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     # E는 간선의 개수
#     # N은 서브트리의 루트
#     E, N = map(int, input().split())
#     V = E + 1 # 마지막 정점 번호
#
#     arr = list(map(int, input().split()))
#
#     # 부모를 인덱스로 자식번호 저장
#     left = [0] * (V + 1)
#     right = [0] * (V + 1)
#
#     for i in range(E):
#         p, c = arr[i * 2], arr[i * 2 + 1]
#         if left[p] == 0:
#             left[p] = c
#         else:
#             right[p] = c
#
#     # print(left)
#     # print(right)
#
#
#     cnt = 0
#     pre_order(N)





#1 3
#2 1
#3 3