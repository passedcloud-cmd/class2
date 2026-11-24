import sys
sys.stdin = open("전기자동차_충전소2.txt")

T = int(input())
for test_case in range(1, T + 1):
    # N은 집의 개수
    N = int(input())

    # 각 집의 x, y 좌표와 허용 거리 d를 담을 리스트 
    homes = [] # [x, y, d]
    # 각 집의 x, y 좌표를 담을 세트
    home_pos = set() #(x, y)
    for _ in range(N):
        x, y, d = map(int, input().split())
        homes.append([x, y, d])
        home_pos.add((x, y))

    min_dist = float('inf') # 최소 거리 합은 무한대로 시작
    # candidate는 충전소에서 집까지의 거리 집합을 모으는 리스트. 충전소가 2개일 때를 위해 준비.
    candidates = [] # N이 3일 때 [[d1, d2, d3], [d4, d5, d6] ...]

    # 경우 1) 충전소 1개가 1개
    # x, y 좌표의 범위는 -15 ~ 15
    # 충전소의 좌표 (i, y)
    for i in range(-15, 16):
        for j in range(-15, 16):
            # 집이 지어진 위치에는 충전소를 못 지으니까 스킵
            if (i, j) in home_pos:
                continue

            total_dist = 0 # 거리 총합
            ok = 0 # 허용 범위 안에 있는 집의 개수. ok == N 이면 성공
            dists = [] # 충전소에서 집까지의 거리를 모은 리스트

            # 충전소에서 집까지의 거리 계산하기 
            for x, y, d in homes:
                dist = abs(i - x) + abs(j - y)
                dists.append(dist) 
                if dist <= d: # 거리가 허용 범위 내라면
                    total_dist += dist
                    ok += 1

            if ok > 0: # 허용 범위 안에 있는 집이 1개라도 있다면
                candidates.append(dists) # 후보군 candidates 리스트에 dists 리스트 추가

            if ok == N: # ok가 집의 개수 N과 같으면 성공
                min_dist = min(min_dist, total_dist)

    # 경우 2) 충전소가 1개로 부족하니 2개라고 가정
    if min_dist == float('inf'):
        # 허용 거리가 가장 작은 집 번호 찾기
        t = 0
        for n in range(N):
            if homes[n][2] < homes[t][2]:
                t = n

        for charge1 in candidates:
            # 첫 번째 충전소는 t번 집을 담당해야 함. 
            if charge1[t] > homes[t][2]: # 첫 번째 충전소가 t번 집을 충전 못하면 스킵
                continue
            for charge2 in candidates:
                # 초기화하고 시작
                total_dist = 0 
                ok = 0 

                for n in range(N):
                    # 두 충전소 중에 가까운 충전소의 거리를 선택
                    dist = min(charge1[n], charge2[n])

                    # 실패한 경우거나 가지 치기 대상이면 스킵
                    if dist > homes[n][2] or total_dist + dist >= min_dist:
                        break # for n

                    total_dist += dist
                    ok += 1

                if ok == N: # ok가 집의 개수면 성공
                    min_dist = total_dist

    # 충전소 2개로도 안 되면 -1을 출력
    if min_dist == float('inf'):
        min_dist = -1

    print(f'#{test_case} {min_dist}')




# import sys
# sys.stdin = open("전기자동차_충전소2.txt")
# T = int(input())
# for test_case in range (1, T+1):
#     # N은 집의 개수
#     N = int(input())
#     # 각 집의 (x좌표, y좌표, 집에서 충전소까지 허용 가능한 거리 d)
#     input_maps = [list(map(int, input().split())) for _ in range(N)]

#     home_locations = [] # 집의 (x, y) 좌표만 기록한 리스트
#     for i in range(N):
#         home_locations.append([input_maps[i][0], input_maps[i][1]])

#     min_dist = float('inf') # 최소 거리합은 무한대로 설정하고 시작
#     candidates_dists = [] # 충전소가 2개일 때를 대비: 각 충전소 후보군과 집까지의 거리를 기록한 리스트 만듦

#     ####### 경우1) 충전소는 1개라고 가정 ########
#     # 맵의 x,y 좌표 범위: -15 ~ 15 / 충전소 좌표는 (i, j)
#     for i in range(-15, 16):
#         for j in range(-15, 16):
#             total_dist = 0 # 충전소와 집까지의 거리 합
#             charge_number = 0 # 충전 가능한 집의 개수. charge_number = N이어야 성공
#             tmp_dist_list = [] # candidates_dists를 채우기 위해 일시적으로 만든 리스트
            
#             # 집 위치엔 충전소를 못 짓는다
#             if [i, j] in home_locations:
#                 continue # 스킵

#             # 충전소와 집까지의 거리를 계산해보자
#             for n in range(N):
#                 dist = abs(i - input_maps[n][0]) + abs(j - input_maps[n][1])
#                 if dist <= input_maps[n][2]: # dist가 허용 가능한 거리 d 이하라면 
#                     total_dist += dist
#                     charge_number += 1 
#                 tmp_dist_list.append(dist) # 각 집과 충전소까지의 거리 모아두기

#             # 충전소가 2개일 때를 대비: 각 충전소 후보군과 집까지의 거리를 기록한 리스트 만듦
#             if charge_number > 0: # 충전 가능한 집이 1개라도 있으면 후보군 리스트에 넣기 
#                 candidates_dists.append(tmp_dist_list) 

#             # 충전기 1개로 모든 집에 접근 가능하다면 성공
#             if charge_number == N:
#                 if total_dist < min_dist: 
#                     min_dist = total_dist

#     ####### 경우2) 충전기 1개로 부족하다면 충전기 2개로 두기 ########
#     if min_dist == float('inf'): 

#         # d가 가장 작은 집 찾기
#         min_idx = 0 # 0번째 집의 d가 제일 작다고 가정
#         for n in range(N):
#             if input_maps[n][2] < input_maps[min_idx][2]:
#                 min_idx = n # n번째 집의 d가 제일 작다고 경신

#         first_candidates = []
#         for candidates_dist in candidates_dists:
#             if candidates_dist[min_idx] <= input_maps[min_idx][2]:
#                 first_candidates.append(candidates_dist)

#         # 충전소를 둘 수 있는 후보군 charge_candidates에서 2개를 골라서 거리 계산
#         for a in range(len(first_candidates)):
#             for b in range(len(candidates_dists)): 
#                 total_dist = 0 # 거리 리셋
#                 charge_number = 0 # 충전 가능 횟수도 리셋

#                 # 2개의 충전소와 집까지의 거리 중 최단 거리 선택
#                 for n in range(N):
#                     dist = min(first_candidates[a][n], candidates_dists[b][n])

#                     # dist가 충전소까지의 허용 거리 d 내에 있다면
#                     if dist <= input_maps[n][2]:
#                         total_dist += dist
#                         charge_number += 1

#                     # 허용 거리 내에 없다면 다음 충전소 후보로 스킵
#                     else:
#                         break # for n

#                     # 가지치기: total_dist가 이미 min_dist 값을 넘어섰다면 더 볼 필요 없으니까 스킵
#                     if total_dist >= min_dist:
#                         break # for n

#                 #  charge_number == N이면 성공
#                 if charge_number == N:
#                     if total_dist < min_dist:
#                         min_dist = total_dist

#     # 만약 모든 충전소 2개로도 모든 집을 돌 수 없다면 -1을 출력
#     if min_dist == float('inf'):
#         min_dist = -1

#     print(f'#{test_case} {min_dist}')




#1 2
#2 3
#3 36
#4 -1
#5 21

#1 3
#2 2
#3 -1
#4 8
#5 11
#6 13
#7 120
#8 4
#9 10
#10 36
#11 311
#12 -1
#13 2
#14 17
#15 20
#16 10
#17 22
#18 58
#19 95
#20 133
#21 263
#22 14
#23 25
#24 52
#25 73
#26 128
#27 185
#28 -1
#29 -1
#30 -1






# ##### 시간 복잡도를 고려해서 수정한 코드 ######
# import sys
# sys.stdin = open("전기자동차_충전소2.txt")
# T = int(input())
# for test_case in range (1, T+1):
#     # N은 집의 개수
#     N = int(input())
#     # 각 집의 x, y 좌표와 충전소까지 허용 가능한 거리 x,y,d
#     input_maps = [list(map(int, input().split())) for _ in range(N)]

#     # 집의 x, y 좌표만 모아놓은 리스트
#     home_locations = []
#     for i in range(N):
#         home_locations.append([input_maps[i][0], input_maps[i][1]])

#     min_dist = float('inf') # 최소 거리합은 무한대로 두고 시작
#     charge_candidates = [] # 충전소가 2개일 때를 대비: 충전소 후보군 리스트 만듦

#     #### 충전소는 1개라고 가정 ####
#     # 완전탐색으로 충전소 위치 찾기 : x, y 좌표 범위는 -15 ~ 15 / 충전소 좌표는 (i, j) 
#     for i in range(-15, 16):
#         for j in range(-15, 16):
#             total_dist = 0
#             charge_number = 0 # 충전 가능한 집 개수. charge_number = N 이어야 성공

#             # 집 위치엔 충전소를 못 짓는다
#             if [i, j] in home_locations:
#                 continue

#             # 충전소와 집의 거리를 계산
#             for n in range(N):
#                 dist = abs(i - input_maps[n][0]) + abs(j - input_maps[n][1])
#                 if dist <= input_maps[n][2]: 
#                     total_dist += dist
#                     charge_number += 1
                    
#             # 충전소가 2개일 때를 대비: 충전소 후보군 리스트 경신
#             if charge_number > 0: # 충전 가능한 집이 1개라도 있으면 후보군 넣기
#                 charge_candidates.append([i, j]) 

#             # 충전기 1개로 모든 집에 접근 가능하다면 min_dist 경신
#             if charge_number == N:
#                 if total_dist < min_dist:
#                     min_dist = total_dist

#     #### 충전기 1개로 부족하다면 충전기 2개로 두기 ####
#     if min_dist == float('inf'): 
#         # 충전소를 둘 수 있는 후보군 charge_candidates에서 2개를 골라 거리 계산
#         for a in range(len(charge_candidates)):
#             for b in range(a + 1, len(charge_candidates)): 
#                 total_dist = 0 
#                 charge_number = 0 # 충전 가능한 집 개수. charge_number = N 이어야 성공

#                 # 충전소와 집까지의 거리 계산
#                 for n in range(N):
#                     dist1 = abs(charge_candidates[a][0] - input_maps[n][0]) + abs(charge_candidates[a][1] - input_maps[n][1])
#                     dist2 = abs(charge_candidates[b][0] - input_maps[n][0]) + abs(charge_candidates[b][1] - input_maps[n][1])
#                     dist = min(dist1, dist2) # 둘 중에 최단 거리를 선택

#                     # dist가 d 이하라면 
#                     if dist <= input_maps[n][2]:
#                         total_dist += dist
#                         charge_number += 1

#                     # 허용 거리 내에 없다면 다음 충전소 후보로 넘어가기
#                     else:
#                         break # for n

#                     # 가지치기: total_dist가 이미 min_dist 값을 넘어섰다면 더 볼 필요 없음
#                     if total_dist >= min_dist:
#                         break # for n

#                 # 모든 집에 접근 가능하다면 min_dist 경신
#                 if charge_number == N:
#                     if total_dist < min_dist:
#                         min_dist = total_dist

#     # 만약 충전소 2개로도 모든 집을 방문할 수 없다면 -1을 출력
#     if min_dist == float('inf'):
#         min_dist = -1

#     print(f'#{test_case} {min_dist}')




# ### 시간 복잡도를 고려하지 않은 코드 ###
# ### 삭제 예정
# import sys
# sys.stdin = open("전기자동차_충전소1.txt")
# T = int(input())
# for test_case in range (1, T+1):
#     # N은 집의 개수
#     N = int(input())
#     # 각 집의 x,y,d(충전소까지 허용 가능한 거리)
#     input_maps = [list(map(int, input().split())) for _ in range(N)]

#     # 각 집의 x,y 
#     home_position = []
#     for i in range(N):
#         home_position.append([input_maps[i][0], input_maps[i][1]])

#     # 완전 탐색
#     min_dist = float('inf')
#     charge_candidates = [] # 충전소를 지을 수 있는 위치 후보군

#     # x, y 범위는 -15 ~ 15
#     # 충전소 좌표는 (i, j)
#     # 경우1) 충전소는 1개라고 가정 
#     for i in range(-15, 16):
#         for j in range(-15, 16):
#             total_dist = 0
#             ok = 0 # 충전 가능한 집 개수. 집의 개수 N과 같아야 성공.

#             # 집이 있는 위치엔 충전소를 못 지으니까 스킵
#             if [i, j] in home_position:
#                 continue

#             else:
#                 charge_candidates.append([i, j]) # 충전소 위치 후보군에 i, j 추가

#             # 충전소와 집의 거리 계산
#             for n in range(N):
#                 dist = abs(i - input_maps[n][0]) + abs(j - input_maps[n][1])
#                 # dist가 각 집의 허용 거리 d 이하라면 성공
#                 if dist <= input_maps[n][2]:
#                     total_dist += dist
#                     ok += 1

#                 # 아니라면 중지
#                 else:
#                     break # for n

#             # ok의 값이 집의 개수 N과 같다면 조건 만족
#             if ok == N:
#                 # 최소 거리합 경신
#                 min_dist = min(total_dist, min_dist)

#     # 경우2) 충전기 2개로
#     if min_dist == float('inf'):
#         # 충전소를 둘 수 있는 위치 후보군 charge_candidates에서 2개를 골라 거리 계산
#         for k in charge_candidates:
#             for l in charge_candidates: 
#                 total_dist = 0 # 거리 합계 리셋
#                 ok = 0 # 충전 가능한 집 개수도 리셋

#                 # 충전소와 집까지의 거리 계산
#                 for n in range(N):
#                     dist1 = abs(k[0] - input_maps[n][0]) + abs(k[1] - input_maps[n][1])
#                     dist2 = abs(l[0] - input_maps[n][0]) + abs(l[1] - input_maps[n][1])
#                     # 더 짧은 거리를 선택
#                     dist = min(dist1, dist2)

#                     # dist가 허용 거리 d 이하라면 성공
#                     if dist <= input_maps[n][2]:
#                         total_dist += dist
#                         ok += 1

#                     # 아니면 스킵
#                     else:
#                         break # for n

#                 # ok == N 이면 조건 만족
#                 if ok == N:
#                     # 최소 거리합 경신
#                     min_dist = min(total_dist, min_dist) 

#     # 만약 모든 충전소 2개로도 모든 집을 충전할 수 없다면 -1을 출력
#     if min_dist == float('inf'):
#         min_dist = -1

#     print(f'#{test_case} {min_dist}')
