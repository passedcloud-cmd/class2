import sys
sys.stdin = open("전기자동차_충전소.txt")
T = int(input())
for test_case in range (1, T+1):
    # N은 집의 개수
    N = int(input())
    # 각 집의 위치 x,y,d(충전소까지 허용 가능한 거리)
    home_maps = [list(map(int, input().split())) for _ in range(N)]

    home_locations = []
    for i in range(N):
        home_locations.append([home_maps[i][0], home_maps[i][1]])


    # 완전 탐색
    min_dist = float('inf')
    charge_candidates = []


    # 맵은 x,y 좌표가 -15 ~ 15
    # 충전소 좌표는 (i, j)
    # 충전소는 1개라고 가정 
    for i in range(-15, 16):
        for j in range(-15, 16):
            total_dist = 0
            charge_number = 0 # 충전 횟수. 충전 횟수와 집의 개수 N이 같아야 충전소 1개로 충분.

            # 집 위치엔 충전소를 못 짓는다
            if [i, j] in home_locations:
                continue
            # 충전소를 둘 수 있는 후보군
            else:
                charge_candidates.append([i, j])


            # 충전소와 집의 거리 계산해보자
            for n in range(N):
                dist = abs(i - home_maps[n][0]) + abs(j - home_maps[n][1])
                if dist <= home_maps[n][2]:
                    total_dist += dist
                    charge_number += 1
                    
                else:
                    break # for n

            # 충전기 1개로 모든 집에 접근 가능하다면
            if charge_number == N:
                if total_dist < min_dist:
                    min_dist = total_dist

            # 충전기 1개로 부족하다면 충전기 2개로 두기
            else:
                # 충전소를 둘 수 있는 후보군 charge_candidates에서 2개를 골라 거리 계산
                for i in charge_candidates:
                    for j in charge_candidates: 
                        total_dist = 0 # 거리 리셋
                        charge_number = 0 # 충전 횟수도 리셋

                        # 충전소와 집까지의 거리
                        for n in range(N):
                            dist1 = abs(i[0] - home_maps[n][0]) + abs(i[1] - home_maps[n][1])
                            dist2 = abs(j[0] - home_maps[n][0]) + abs(j[1] - home_maps[n][1])
                            dist = min(dist1, dist2)

                            # 충전소까지의 허용 거리 내에 있다면
                            if dist <= home_maps[n][2]:
                                total_dist += dist
                                charge_number += 1

                            else:
                                break # for n
                        if charge_number == N:
                            if total_dist < min_dist:
                                min_dist = total_dist
                        # 만약 모든 충전소 2개로도 모든 집을 돌 수 없다면 -1을 출력
                        else:
                            min_dist = -1



    print(f'#{test_case} {min_dist}')




#1 2
#2 3
#3 36
#4 -1
#5 21