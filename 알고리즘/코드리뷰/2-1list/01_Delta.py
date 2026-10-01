import sys
sys.stdin = open("01_Delta.txt")

T = int(input())


for tc in range(1, T + 1):
    # N은 행과 열의 개수. 행렬의 shpae가 N x N
    N = int(input()) 

    # arr에 주어진 값들을 넣어 행렬 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우 방향 설정하기
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    direction_name = ["상", "하", "좌", "우"]

    # result는 0으로 시작
    result = 0

    # 행을 기준으로 모든 요소 꺼내기
    for r in range(N):
        for c in range(N):
            # 각 요소마다 상하좌우 이웃들 꺼내기 
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                # 경계 체크
                if 0 <= nr < N and 0 <= nc < N:
                    sum_abs_number = arr[nr][nc] - arr[r][c]
                    # 절댓값 처리
                    if sum_abs_number < 0:
                        sum_abs_number = -sum_abs_number
                    result += sum_abs_number

    print(f"#{tc} {result}")