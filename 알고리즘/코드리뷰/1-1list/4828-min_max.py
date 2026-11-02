import sys
sys.stdin = open("4828-min_max.txt")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_number = arr[0]
    min_number = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_number:
            max_number = arr[i]

        if arr[i] < min_number:
            min_number = arr[i]

    print(f'#{test_case} {max_number - min_number}')





















# import sys
#
# sys.stdin = open('4828-min_max.txt')
#
# T = int(input()) #3
#
# for t in range(T): # T=3번 반복
#     N = int(input())
#     arr = list(map(int, (input().split())))
#
#     for _ in range(N):
#         # 최솟값과 최댓값은 임의로 첫 번째 값으로 배정
#         min_num = arr[0]
#         max_num = arr[0]
#         for j in arr:
#             # 반복문을 돌면서 최솟값과 최댓값을 갱신
#             if min_num > j:
#                 min_num = j
#
#             if max_num < j:
#                 max_num = j
#     print(f"#{t+1} {max_num - min_num}")


# 오답노트 
# min_num = arr[0]와 max_num = arr[0]가 for j in arr: 안에 있어서 한 바퀴 돌 때마다 값이 리셋됨.

# 정답 예시
#1 630739
#2 740510
#3 838110