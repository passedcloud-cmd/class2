import sys
sys.stdin = open('5177-이진힙.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    heap = [0] * (N+1)

    def enqueue(node):
        global last
        last +=1
        heap[last] = node
        c_idx = last
        p_idx = last // 2
        while p_idx and heap[c_idx] < heap[p_idx]:
            heap[c_idx], heap[p_idx] = heap[p_idx], heap[c_idx]
            c_idx = p_idx
            p_idx = c_idx // 2

    def dequeue():
        global last
        tmp = heap[0]
        heap[0] = heap[last]
        last -= 1
        p_idx = 1
        c_idx = p * 2
        while c_idx <=last:
            if c_idx + 1 <=last and heap[c_idx] > heap[c_idx +1]:
                c_idx = c_idx+1
            if heap[p_idx] > heap[c_idx]:
                heap[p_idx], heap[c_idx] =  heap[c_idx], heap[p_idx]
                p_idx = c_idx
                c_idx = p_idx * 2
            else:
                break

        return tmp

    numbers = list(map(int, input().split()))
    last = 0
    for new_node in numbers:
        enqueue(new_node)

    # print(heap)

    sum = 0
    tmp = heap[last]
    while last > 0:
        sum += heap[last]
        last = last//2

    print(f'#{test_case} {sum - tmp}')



# 오답노트
    # par = last//2
    # print(par)
    # par = last//2
    # print(par)
    # par = last//2
    # print(par) 
    # par는 전부 같은 수. 






# import sys
# sys.stdin = open('5177.txt')

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     def enq(n):
#         global last
#         # 마지막 정점 추가
#         last += 1  # 마지막 정점 추가
#         heap[last] = n  # 마지막 정점에 추가

#         # 최소힙 : 부모 < 자식
#         c = last
#         p = c // 2
#         # 부모가 있고, 부모 > 자식 이면 교환
#         while p and heap[p] > heap[c]:
#             heap[p], heap[c] = heap[c], heap[p]
#             c = p  # 부모와 부모의 부모를 비교
#             p = c // 2


#     heap = [0] * (N + 1) # 정점이 N개인 완전 이진 트리
#     last = 0 # 마지막 정점 번호

#     for x in arr:
#         enq(x)

#     print(heap)

#     ans = 0
#     c = last
#     while c // 2 > 0:
#         c //= 2
#         ans += heap[c]

#     print(ans)



# 7
# 5
# 65