import sys
sys.stdin = open('1206_view.txt')
T = 10 # 문제에 주어짐
for test_case in range(1, T + 1):
    # N은 건물 개수
    N = int(input())
    # 건물 배열
    arr = list(map(int, input().split()))

    sum_total = 0
    # 왼쪽으로 두 건물과 오른쪽으로 두 건물 높이 차이를 구한 다음
    # 높이차가 가장 작은 값이 조망권 확보 가구 수
    for i in range(2, N - 2):
        left_2 = arr[i] - arr[i - 2]
        left_1 = arr[i] - arr[i - 1]
        right_1 = arr[i] - arr[i + 1]
        right_2 = arr[i] - arr[i + 2]

        # 높이차를 리스트에 넣고
        # 최솟값 구하기
        # 최솟값이 음수면 0으로 처리
        height_difference = [left_2, left_1, right_1, right_2]
        min_height_difference = height_difference[0]
        for j in range(len(height_difference)):
            if height_difference[j] < min_height_difference:
                min_height_difference = height_difference[j]

        if min_height_difference < 0:
            min_height_difference = 0

        sum_total += min_height_difference

    print(f'#{test_case} {sum_total}')
























# import sys
# sys.stdin = open("1206_view.txt")
#
# # test_case가 10이라고 문제에 주어짐
# T = 10
#
# for test_case in range(1, T + 1):
#     # 건물의 개수 N
#     N = int(input())
#
#     # 각 건물의 높이
#     each_height = list(map(int, input().split()))
#
#     # 조망권 보장된 층의 개수
#     result_counting = 0
#
#     # n번째 건물에서 왼쪽 두 건물과 오른쪽 두 건물의 높이차를 각각 구하기
#     # 높이차 4개가 전부 양수라면 조망권 보장된 층이 있음
#     # 높이차가 가장 작은 수 = 조망권 보장된 층의 수
#     for n in range(2, N - 2):
#         # 높이차 4번 구하기
#         left_2 = each_height[n] - each_height[n - 2]
#         left_1 = each_height[n] - each_height[n - 1]
#         right_2 = each_height[n] - each_height[n + 2]
#         right_1 = each_height[n] - each_height[n + 1]
#
#         # 높이차 4개가 모두 양수 -> n번째 건물이 가장 높다 -> 조망권 보장된 층이 있다
#         if left_2 > 0 and left_1 > 0 and right_2 > 0 and right_1 >0 :
#
#             #최솟값 구하기
#             height_arr = [left_2, left_1, right_1, right_2]
#             min_height = height_arr[0] # 최솟값 임의로 할당
#             for i in height_arr:
#                 if min_height > i:
#                     min_height = i
#
#             # 조망권 보장 층수 누적
#             result_counting += min_height
#
#     print(f'#{test_case} {result_counting}')



# 출력
#1 691
#2 9092
#3 8998
#4 9597
#5 8757
#6 10008
#7 10194
#8 10188
#9 9940
#10 8684