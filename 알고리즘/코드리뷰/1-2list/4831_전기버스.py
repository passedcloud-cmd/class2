import sys
sys.stdin = open('4831_전기버스.txt')
# T는 노선 수(test_case)
T = int(input())

for test_case in range(1, T + 1):
    # K는 최대한 이동할 수 있는 정류장 수
    # N은 종점
    # M은 충전기가 설치된 개수
    K, N, M = map(int, input().split())

    # 충전기가 있는 정류장 번호
    chargers = list(map(int, input().split()))

    position_now = 0
    charge_count = 0

    # 최대 멀리까지 간 후 되돌아오면서 정류장 있는지 체크
    while position_now + K < N:
        for i in range(position_now + K, position_now, -1):
            if i in chargers:
                position_now = i
                charge_count += 1
                break # for i
        # for문을 다 돌았다는 건 충전기가 있는 정류소를 못 찾았다는 뜻
        else:
            charge_count = 0
            break # for while

    print(f'#{test_case} {charge_count}')
























# # 방법 1:최대치로 전진 후 뒤로 돌아보며 충전소를 찾기. 방법 3와 비슷한 느낌
#     # 모든 정류장 정보를 담을 리스트 생성. 충전소 위치는 1
#     stations = [0] * (N + 1)
#     for i in chargers:
#         stations[i] = 1
#
#     current_position = 0 # 버스의 현재 위치
#     charge_count = 0
#
#     # 버스가 종점에 도달할 때까지 반복
#     while current_position < N:
#         # 현재에서 최대로 갈 수 있는 위치
#         next_position = current_position + K
#
#         # 현재에서 최대치로 이동했지만 종점에 도달하지 못한다면
#         if next_position < N:
#             # next_position부터 현재 위치까지 거꾸로 탐색하며 충전소 찾기
#             for i in range(next_position, current_position, -1):
#                 if stations[i] == 1: # 가장 먼 충전소를 찾으면
#                     current_position = i # 그 충전소로 이동
#                     charge_count += 1
#                     break # 가장 먼 충전소를 찾았으니 break for i
#
#             # 가장 먼 충전소를 찾지 못했다면 fail이므로 0 출력
#             # for문의 else
#             else:
#                 charge_count = 0
#                 break
#         # 만약 next_position >= N라면 더 이상 충전이 필요 없음
#         else:
#             break #for while
#
#     print(f"#{test_case} {charge_count}")


# 방법 2: 충전소 목록을 직접 탐색
    #출발지와 종점도 충전소 목록에 추가하여 계산을 단순화하기.








# # 방법3: 최대 도달 가능 위치를 갱신하면서 한 방향으로만 탐색
# # 멀리 갈 수 있는 곳까지 구한 다음에 거꾸로 돌아오면서 정류장 찾기. 그 정류장이 갈 수 있는 가장 먼 정류장.
# # 만약 갈 수 있는 정류장이 없으면 0 출력
#
#     charge_count = 0
#     bus_position = 0 # 버스의 현재 위치
#
#     while bus_position + K < N:
#         # 현재 위치에서 K만큼 갔을 때 그 안에 충전소가 있는지 확인.
#         farthest_charger = 0 # 가장 멀리 있는 충전소
#         for i in range(bus_position + K, bus_position, -1):
#             if i in chargers:
#                 farthest_charger = i
#                 break # for i
#
#         # 만약 도달 가능한 충전소가 없으면 실패. 0을 출력
#         if farthest_charger == 0:
#             charge_count = 0
#             break # while
#
#         # 가장 먼 충전소로 이동하고 충전 +1
#         bus_position = farthest_charger
#         charge_count += 1
#
#     print(f'#{test_case} {charge_count}')






# 오답노트
# 리스트에 요소 추가 방법
#     sample = [1]
#     test = [0] + sample + [2] + [3, 4]

#출력
#1 3
#2 0
#3 4
#4 0

#입력
# 4
# 3 10 5
# 1 3 5 7 9
# 3 10 5
# 1 3 7 8 9
# 5 20 5
# 4 7 9 14 17
# 5 100 20 
# 6 10 15 20 25 30 35 40 45 50 55 60 65 70 75 76 81 85 90 95