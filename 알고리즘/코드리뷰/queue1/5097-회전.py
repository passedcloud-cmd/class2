import sys
sys.stdin = open("5097-회전.txt")
from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    my_arr = deque(arr)

    for _ in range(M):
        my_arr.rotate(-1)

    result = my_arr.popleft()

    print(f'#{test_case} {result}')









# deque 사용
# import sys
# sys.stdin = open("5097-회전.txt")
# T = int(input())
#
# from collections import deque
#
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     arr_deque = deque(arr)
#
#     for m in range(M):
#         arr_deque.rotate(-1)
#
#     print(f'#{test_case} {arr_deque[0]}')
