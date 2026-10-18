import sys
sys.stdin = open("11기-차르봄바.txt")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # arr는 N x M 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방향키 설정 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 최댓값 설정
    max_destruction = float('-inf')

    # 완전 탐색으로 풀이
    for r in range(N):
        for c in range(M):
            # 한 칸 이동할 때마다 합계 리셋
            sum_destruction = 0
            # 폭탄 위력은 arr[r][c]의 값
            bomb_power = arr[r][c]
            # 일단 해당 영역 파괴됐으니 변수 경신
            sum_destruction += arr[r][c]

            # 폭탄 위력만큼 파괴 지역 추가
            for n in range(bomb_power):
                # 상하좌우 네 방향 추가
                for i in range(4):
                    nr = r + dr[i] * (n + 1)
                    nc = c + dc[i] * (n + 1)
                    # 경계 체크
                    if 0 <= nr < N and 0 <= nc < M:
                        sum_destruction += arr[nr][nc]

            # 파괴 지역 모두 구했으면 최댓값 경신
            if sum_destruction > max_destruction:
                max_destruction = sum_destruction

    print(f'#{test_case} {max_destruction}')



# 출력
# #1 10
# #2 26
# #3 40