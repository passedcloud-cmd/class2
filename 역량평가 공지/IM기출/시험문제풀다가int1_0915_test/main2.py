import sys
sys.stdin = open("Sample_input.txt")
T = int(input())
for test_case in range(1, T + 1):
    # N은 점들의 개수
    # S는 시작점의 좌표
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    # 배열에 S넣기
    arr.append(S)
    # 먼저 배열을 오른차순으로 정렬
    arr_sorted = sorted(arr)

    # 최소값 임의 설정
    min_dis = float('inf')
    dis_sum1 = 0 # 거리 합계는 0으로 시작
    dis_sum2 = 0
    # 배열의 복사본
    arr_sorted1 = arr_sorted[::]
    arr_sorted2 = arr_sorted[::]
    # # 시작점 복사본
    S0 = S


    # arr_sorted 에서 S의 위치
    S1 = arr_sorted1.index(S)
    S2 = arr_sorted2.index(S)
    # print(arr_sorted1)

    # 빈 리스트
    list_check = []
    list_check.append(S0)
    # 점 개수만큼 순회. 1번- 좌우 거리가 같으면 왼쪽 고름
    while arr_sorted1:

        #값이 1개 남음
        if len(arr_sorted1) == 1:
            # dis_sum1 += arr_sorted1[0]
            break # for while

        # 경계 체크
        elif S1 == 0: # 첫 번째 값이면 오른쪽으로 이동
            # 거리 더하기
            dis_sum1 += abs(arr_sorted1[S1] - arr_sorted1[S1 + 1])
            # 이전 점은 제거
            arr_sorted1.remove(arr_sorted1[S1])
            # 점 이동 - 계속 첫 번째 값일 것임
            S1 = 0

        elif S1 == (len(arr_sorted1) - 1): # 마지막 값이면 왼쪽으로 이동
            # 거리 더하기
            dis_sum1 += abs(arr_sorted1[S1] - arr_sorted1[S1 - 1])

            # 이전 점은 제거
            arr_sorted1.remove(arr_sorted1[S1])

            # 점 이동 - 계속 마지막 값일 것임
            S1 = len(arr_sorted1) - 1

        # 현재 위치에서 좌우 비교
        # 오른쪽이 가까우면 오른쪽으로 이동
        elif abs(arr_sorted1[S1] - arr_sorted1[S1 - 1]) > abs(arr_sorted1[S1] - arr_sorted1[S1 + 1]):

            # 거리 더하기
            dis_sum1 += abs(arr_sorted1[S1] - arr_sorted1[S1 + 1])
            temp_value = arr_sorted1[S1 + 1]
            # 이전 점은 제거
            arr_sorted1.remove(arr_sorted1[S1])
            # 점 이동
            S1 = arr_sorted1.index(temp_value)


        # 왼쪽이 가까우면 왼쪽으로 이동
        elif abs(arr_sorted1[S1] - arr_sorted1[S1 - 1]) < abs(arr_sorted1[S1] - arr_sorted1[S1 + 1]):
            # 거리 더하기
            dis_sum1 += abs(arr_sorted1[S1] - arr_sorted1[S1 - 1])
            temp_value = arr_sorted1[S1 - 1]
            # 이전 점은 제거
            arr_sorted1.remove(arr_sorted1[S1])
            # 점 이동
            S1 = arr_sorted1.index(temp_value)


        ########### 만약 좌우 거리가 같으면 왼쪽으로 이동 ######
        elif abs(arr_sorted1[S1] - arr_sorted1[S1 - 1]) == abs(arr_sorted1[S1] - arr_sorted1[S1 + 1]):
            # 거리 더하기
            dis_sum1 += abs(arr_sorted1[S1] - arr_sorted1[S1 - 1])
            temp_value = arr_sorted1[S1 - 1]
            # 이전 점은 제거
            arr_sorted1.remove(arr_sorted1[S1])
            # 점 이동
            S1 = arr_sorted1.index(temp_value)

    #sorted1 준비


################################# 만약 좌우 거리가 같으면 오른쪽으로 이동 ######
    # 빈 리스트
    list_check = []
    list_check.append(S0)
    # 점 개수만큼 순회. 1번- 좌우 거리가 같으면 왼쪽 고름
    while arr_sorted2:

        #값이 1개 남음
        if len(arr_sorted2) == 1:
            # dis_sum1 += arr_sorted1[0]
            break # for while

        # 경계 체크
        elif S2 == 0: # 첫 번째 값이면 오른쪽으로 이동
            # 거리 더하기
            dis_sum2 += abs(arr_sorted2[S2] - arr_sorted2[S2 + 1])

            # 이전 점은 제거
            arr_sorted2.remove(arr_sorted2[S2])
            # 점 이동.
            S2 = 0


        elif S2 == (len(arr_sorted2) - 1): # 마지막 값이면 왼쪽으로 이동
            # 거리 더하기
            dis_sum2 += abs(arr_sorted2[S2] - arr_sorted2[S2 - 1])

            # 이전 점은 제거
            arr_sorted2.remove(arr_sorted2[S2])

            # 점 이동 - 계속 마지막 값
            S2 = len(arr_sorted2) - 1

        # 현재 위치에서 좌우 비교
        # 오른쪽이 가까우면 오른쪽으로 이동
        elif abs(arr_sorted2[S2] - arr_sorted2[S2 - 1]) > abs(arr_sorted2[S2] - arr_sorted2[S2 + 1]):

            # 거리 더하기
            dis_sum2 += abs(arr_sorted2[S2] - arr_sorted2[S2 + 1])
            temp_value = arr_sorted2[S2 + 1]
            # 이전 점은 제거
            arr_sorted2.remove(arr_sorted2[S2])
            # 점 이동
            S2 = arr_sorted2.index(temp_value)




        # 왼쪽이 가까우면 왼쪽으로 이동
        elif abs(arr_sorted2[S2] - arr_sorted2[S2 - 1]) < abs(arr_sorted2[S2] - arr_sorted2[S2 + 1]):
            # 거리 더하기
            dis_sum2 += abs(arr_sorted2[S2] - arr_sorted2[S2 - 1])
            temp_value = arr_sorted2[S2 - 1]
            # 이전 점은 제거
            arr_sorted2.remove(arr_sorted2[S2])

            # 점 이동
            S2 = arr_sorted2.index(temp_value)

        ########### 만약 좌우 거리가 같으면 오른쪽으로 이동 ######
        elif abs(arr_sorted2[S2] - arr_sorted2[S2 - 1]) == abs(arr_sorted2[S2] - arr_sorted2[S2 + 1]):
            # 거리 더하기
            dis_sum2 += abs(arr_sorted2[S2] - arr_sorted2[S2 + 1])
            temp_value = arr_sorted2[S2 + 1]
            # 이전 점은 제거
            arr_sorted2.remove(arr_sorted2[S2])
            # 점 이동
            S2 = arr_sorted2.index(temp_value)



    # print(f'{arr_sorted1}, {arr_sorted2}')
    result = min(dis_sum1, dis_sum2)
    # print(arr_sorted1)

    # print(f'#{test_case} {dis_sum}')
    print(f'{"#%d" % test_case} {result}')







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

# 보험2
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