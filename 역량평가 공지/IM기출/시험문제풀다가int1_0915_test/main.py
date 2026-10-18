import sys
sys.stdin = open("Sample_input.txt")
T = int(input())
for tc in range(1, T + 1):
    N, S = map(int, input().split())
    points = list(map(int, input().split()))

    left = min(points)
    right = max(points)
    span = right - left

    # 후보 A: 시작점 => 왼쪽 끝으로 이동한 뒤, 오른쪽 끝까지 한 방향으로 훑는다
    left_first = abs(S - left) + span

    # 후보 B: 시작점 => 오른쪽 끝으로 이동한 뒤, 왼쪽 끝까지 한 방향으로 훑는다
    right_first = abs(S - right) + span

    # 가능한 최적 경로는 이 둘 중 하나뿐이므로 더 작은 값을 택한다
    print(f'#{tc} {min(left_first, right_first)}')

# 입력
# 4
# 4 5
# 4 8 9 10
# 5 7
# 10 4 8 9 1
# 8 1
# 3 5 10 8 9 12 13 15
# 1 2
# 9
# [출력 예]
# #1 7
# #2 12
# #3 14
# #4 7

##1 7
#2 12
#3 14
#4 7
#5 3
#6 16
#7 58
#8 51
#9 67
#10 75
#11 128
#12 100
#13 105
#14 139
#15 98
#16 86
#17 100
#18 140
#19 125
#20 114
#21 1021
#22 1073
#23 1155
#24 1350
#25 1247
#26 989
#27 1026
#28 1039
#29 1004
#30 1001



Process finished with exit code 0



# #  보험 - 30개중 23개 맞음
# import sys
# sys.stdin = open("input.txt")
# T = int(input())
# for test_case in range(1, T + 1):
#     # N은 점들의 개수
#     # S는 시작점의 좌표
#     N, S = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     # 먼저 배열을 오른차순으로 정렬
#     arr_sorted = sorted(arr)
#
#     print(f'시작점S: {S}/ 정렬: {arr_sorted}')
#
#     # 최소값 임의 설정
#     min_dis = float('inf')
#     dis_sum = 0 # 거리 합계는 0으로 시작
#     # 점 개수만큼 순회
#     for i in range(N):
#
#         # 시작점으로부터 가장 가까운 점을 찾아야 함
#         min_dis_temp = float('inf')
#         for j in range(len(arr_sorted)):
#             temp_dis = abs(S - arr_sorted[j])
#             if temp_dis < min_dis_temp:
#                 min_dis_temp = temp_dis
#                 next_dot = arr_sorted[j] # j는 다음으로 이동할 점
#         # 다음으로 이동할 점은 리스트에서 빼버리기
#         arr_sorted.remove(next_dot)
#
#         dis_sum += abs(S - next_dot)
#         # 이동했으므로 S의 위치도 변해야 함
#         S = next_dot
#
#     # print(f'#{test_case} {dis_sum}')
#     print(f'{"#%d" % test_case} {dis_sum}')


#############################################

##보험2
# import sys
# sys.stdin = open("Sample_input.txt")
# T = int(input())
# for test_case in range(1, T + 1):
#     # N은 점들의 개수
#     # S는 시작점의 좌표
#     N, S = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     # 먼저 배열을 오른차순으로 정렬
#     arr_sorted = sorted(arr)
#
#     # print(f'시작점 S: {S}/ 정렬: {arr_sorted}')
#
#
#
#     # 시작점으로부터 가장 가까운 점을 찾아야 함
#     # 좌우의 거리가 똑같이 가까운 경우, 좌로 이동했을 때의 결과와 우로 이동했을 때의 결과를 둘 다 구한 다음 마지막에 비교
#
#     # 최소값 임의 설정
#     min_dis = float('inf')
#     dis_sum1 = 0 # 거리 합계는 0으로 시작
#     dis_sum2 = 0
#     # 배열의 복사본
#     arr_sorted1 = arr_sorted[::]
#     arr_sorted2 = arr_sorted[::]
#     # 시작점 복사본
#     S1 = S
#     S2 = S
#     # 점 개수만큼 순회. 1번- 좌우 거리가 같으면 왼쪽 고름
#     for i in range(N):
#
#         # 시작점으로부터 가장 가까운 점 찾기
#         min_dis_temp = float('inf')
#         for j in range(len(arr_sorted1)):
#             temp_dis = abs(S1 - arr_sorted1[j])
#             if temp_dis < min_dis_temp:
#                 min_dis_temp = temp_dis
#                 next_dot1 = arr_sorted1[j] # j는 다음으로 이동할 점
#         # 다음으로 이동할 점은 리스트에서 빼버리기
#         arr_sorted1.remove(next_dot1)
#
#         dis_sum1 += abs(S1 - next_dot1)
#         # 이동했으므로 S의 위치도 변해야 함
#         S1 = next_dot1
#
#     # 점 개수만큼 순회. 2번- 좌우 거리가 같으면 오른쪽 고름
#     for i in range(N):
#
#         min_dis_temp = float('inf')
#         for j in range(len(arr_sorted2)):
#             temp_dis = abs(S2 - arr_sorted2[j])
#             if temp_dis <= min_dis_temp:
#                 min_dis_temp = temp_dis
#                 next_dot2 = arr_sorted2[j] # j는 다음으로 이동할 점
#         # 다음으로 이동할 점은 리스트에서 빼버리기
#         arr_sorted2.remove(next_dot2)
#
#         dis_sum2 += abs(S2 - next_dot2)
#         # 이동했으므로 S의 위치도 변해야 함
#         S2 = next_dot2
#
#     result = min(dis_sum1, dis_sum2)
#
#     # print(f'#{test_case} {dis_sum}')
#     print(f'{"#%d" % test_case} {result}')