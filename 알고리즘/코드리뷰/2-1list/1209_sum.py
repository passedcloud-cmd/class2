import sys
sys.stdin = open("1209_sum.txt")
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    # 100 x 100 배열
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_max = 0

    # 각 행의 합
    for row in arr:
        sum_row = 0
        for i in row:
            sum_row += i
            if sum_row > sum_max:
                sum_max = sum_row

    # 각 열의 합
    for j in range(100):
        sum_column = 0
        for row in arr:
            sum_column += row[j]
        if sum_column > sum_max:
            sum_max = sum_column

    # 대각선 합
    sum_diagonal1 = 0
    sum_diagonal2 = 0
    for d in range(100):
        sum_diagonal1 += arr[d][d]
        if sum_diagonal1 > sum_max:
            sum_max = sum_diagonal1

        sum_diagonal2 += arr[99 - d][99 - d]
        if sum_diagonal2 > sum_max:
            sum_max = sum_diagonal2

    print(f'#{test_case} {sum_max}')






























# import sys
# sys.stdin = open("1209_sum.txt")
#
# # test_case는 10개라고 문제에 명시
# T = 10
# for test_case in range(T):
#     # N은 test_case 번호
#     N = int(input())
#
#     # 100 x 100 배열 arr 만들기
#     arr = [list(map(int, input().split())) for _ in range(100)]
#
#     # 최댓값은 0이라고 임의로 정하고 시작
#     max_sum = 0
#
#     # 행의 합계 100개 구하기
#     for r in range(100):
#         # 행이 바뀔 때마다 행의 합계 초기화
#         sum_row = 0
#         for c in range(100):
#             sum_row += arr[r][c]
#         if sum_row > max_sum:
#             max_sum = sum_row
#
#     # 열의 합계 100개 구하기
#     for c in range(100):
#         # 열이 바뀔 때마다 열의 합계 초기화
#         sum_column = 0
#         for r in range(100):
#             sum_column += arr[r][c]
#         if sum_column > max_sum:
#             max_sum = sum_column
#
#     # 왼->오 대각선 합계 구하기
#     # 시작 전에 대각선 합계 초기화
#     sum_diagonal_left = 0
#     for c in range(100):
#         sum_diagonal_left += arr[c][c]
#         if sum_diagonal_left > max_sum:
#             max_sum = sum_diagonal_left
#
#     # 오->왼 대각선 합계 구하기
#     sum_diagonal_right = 0
#     for c in range(100):
#         sum_diagonal_right += arr[c][c]
#         if sum_diagonal_right > max_sum:
#             max_sum = sum_diagonal_right
#
#     print(f'#{N} {max_sum}')



# 출력
# #1 1712
# #2 1743
# #3 1713