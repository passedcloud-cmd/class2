# # 첫 번째 test_case 이동 경로 해석
# # P = [0, 1, 1, 2, 0]
# # 1번(인덱스0)에서 2번(인덱스1) 방으로 이동
# # 1번(인덱스0)으로 이동
# # 2번'(인덱스1)으로 이동
# # 3번(인덱스2)으로 이동
# # 1번(인덱스0)으로 이동
# # 2번'(인덱스1)으로 이동
# # 3번'(인덱스2)으로 이동
# # 4번(인덱스3)으로 이동
# # 2번'(인덱스1)르로 이동
# # 3번'(인덱스2)으로 이동
# # 4번'(인덱스3)으로 이동
# # 5번(인덱스4)으로 이동 - 마지막 방 도착
# # -> 12번 이동
#
# import sys
# sys.stdin = open("14기-포탈.txt")
# T = int(input())
# for test_case in range(1, T + 1):
#     # N은 방의 개수
#     N = int(input())
#     # P[i]
#     P = list(map(int, input().split()))
#
#     # 방 번호는 (인덱스 + 1)
#     # 그러므로 왼쪽으로 이동할 땐 P[i] - 1로 이동해야 함
#     # 빈 딕셔너리를 만들기. key는 방 번호(인덱스 + 1), value는 P[인덱스]
#         # 마지막 방(N-1)으로 이동할 때까지 while문 반복
#         # 딕셔너리에 방 번호가 비어있으면 P[i]-1으로 이동 후, 방 번호를 key에 추가
#         # 딕셔너리에 방 번호가 있으면 오른쪽으로 1칸 이동
#         # 한 번 이동할 때마다 카운트 +1 누적
#
#     # 빈 딕셔너리를 만들기
#     move_check = {} # key는 방 번호(=인덱스 + 1), value는 P[인덱스]
#     move_count = 0 # 이동횟수는 0부터 시작
#     now_index = 0 # 현재 위치를 나타는 인덱스 번호. 0부터 시작
#
#     # 인덱스(N-1)까지 이동하면 종료. now_index를 사용할 것.
#     while now_index != N - 1:
#
#         # 딕셔너리에 방 번호가 없으면 딕셔너리에 방 번호인 (now_index + 1)과 P[now_index]를 key-value로 추가
#         if (now_index + 1) not in move_check:
#             move_check[now_index + 1] = P[now_index]
#             # 만약 방 번호(now_index + 1)가 1이라면 오른쪽으로 이동 (1번째 방이면 무조건 오른쪽으로 이동이라고 문제에 명시)
#             if (now_index + 1) == 1:
#                 now_index += 1 # 오른쪽 이동
#                 # 이동 후 이동횟수 +1
#                 move_count += 1
#             # 만약 방 번호(now_index + 1)가 1이 아니라면 P[now_index] -1 으로 왼쪽 이동
#             else:
#                 now_index = P[now_index] - 1
#                 # 이동 후 이동횟수 +1
#                 move_count += 1
#
#         # 딕셔너리에 방 번호가 있으면 오른쪽으로 1칸 이동
#         else:
#             now_index += 1
#             # 이동 후 이동횟수 +1
#             move_count += 1
#
#     print(f'#{test_case} {move_count}')


# 딕셔너리가 아니라 리스트를 만드는 게 더 좋음
# 딕셔너리를 만들어봤자 key만 조회하고 value는 안 쓰기 때문

import sys
sys.stdin = open("14기-포탈.txt")
T = int(input())
for test_case in range(1, T + 1):
    # N은 방의 개수
    N = int(input())
    # P[i]
    P = list(map(int, input().split()))

		# i는 인덱스 번호
    # 방 번호는 (i + 1)
	    # 예시: 1번째 방의 인덱스 번호는 0
    # 그러므로 왼쪽으로 이동할 땐 P[i] - 1로 이동해야 함
    # 빈 리스트를 만들기. 요소는 방 번호(= i + 1)
        # 마지막 방(N-1)으로 이동할 때까지 while문 반복
        # 리스트에 방 번호가 비어있으면 P[i] - 1로 이동 후, 방 번호를 key에 추가
        # 리스트에 방 번호가 있으면 오른쪽으로 1칸 이동
        # 한 번 이동할 때마다 카운트 +1 누적

    # 빈 리스트 만들기
    move_check = [] # 요소는 방 번호(= i + 1)
    move_count = 0 # 이동횟수는 0부터 시작
    now_index = 0 # 현재 위치를 나타는 인덱스 번호. 0부터 시작

    # 인덱스(N-1)까지 이동하면 종료. now_index를 사용할 것.
    while now_index != N - 1:

        # 리스트에 방 번호가 없으면 방 번호인 (now_index + 1) 추가
        if (now_index + 1) not in move_check:
            move_check.append(now_index + 1)
            # 만약 방 번호(now_index + 1)가 1이라면 오른쪽으로 이동 (1번째 방이면 무조건 오른쪽으로 이동이라고 문제에 명시)
            if (now_index + 1) == 1:
                now_index += 1 # 오른쪽 이동
                # 이동 후 이동횟수 +1
                move_count += 1
            # 만약 방 번호(now_index + 1)가 1이 아니라면 P[now_index] -1 으로 왼쪽 이동
            else:
                now_index = P[now_index] - 1
                # 이동 후 이동횟수 +1
                move_count += 1

        # 리스트에 방 번호가 있으면 오른쪽으로 1칸 이동
        else:
            now_index += 1
            # 이동 후 이동횟수 +1
            move_count += 1

    print(f'#{test_case} {move_count}')


















# 출력
# #1 12
# #2 13
# #3 7
# #4 25
# #5 25
# #6 34
# #7 30
# #8 57
# #9 90
# #10 130
# #11 263
# #12 417
# #13 685
# #14 1363
# #15 2056
# #16 2526
# #17 2815
# #18 4166
# #19 3851
# #20 4895
# #21 5872
# #22 9772
# #23 10797
# #24 23029
# #25 23090
# #26 39495
# #27 41132
# #28 63603
# #29 64564
# #30 65480
