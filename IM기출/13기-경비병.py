import sys
sys.stdin = open("13기-경비병.txt")
T = int(input())
for test_case in range(1, T + 1):
    # N은 행과 열의 크기
    N = int(input())
    # N x N arr
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 완전 탐색 사용
    # 값이 0 인 개수 세기
    # 값이 2인 좌표 찾기
    # 2를 중심으로 상하좌우 끝까지 십자가 범위 내에 있는 0은 카운트에서 빼야 하는데, 1을 만나면 그 방향은 종료

    space_count = 0 # 공간은 0으로 시작

    # 완전 탐색으로 값이 0인 공간 찾기
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                space_count += 1

    # 경비병의 좌표 찾기
    for r in range(N):
        found = False
        for c in range(N):
            if arr[r][c] == 2:
                # 경비병의 좌표 (r1, c1)
                r1 = r
                c1 = c
                # 경비병을 찾았으면 반복문 종료
                found = True
                break # for c
        # 경비병을 찾았으면 반복문 종료
        if found:
            break # for r

    # 방향키 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 우측 보기
    for i in range(N):
        nr = r1 + dr[0] * (i + 1)
        nc = c1 + dc[0] * (i + 1)

        # 경계 체크
        if 0 <= nr < N and 0 <= nc < N:
            # 값이 1이면 벽. 벽을 만나면 해당 방향 break
            if arr[nr][nc] == 1:
                break # for i
            # 벽이 없으면, 즉 값이 0이면 count -1
            else:
                space_count -= 1

    # 아래쪽 보기
    for i in range(N):
        nr = r1 + dr[1] * (i + 1)
        nc = c1 + dc[1] * (i + 1)

        # 경계 체크
        if 0 <= nr < N and 0 <= nc < N:
            # 값이 1이면 벽. 벽을 만나면 해당 방향 break
            if arr[nr][nc] == 1:
                break # for i
            # 벽이 없으면, 즉 값이 0이면 count -1
            else:
                space_count -= 1

    # 좌측 보기
    for i in range(N):
        nr = r1 + dr[2] * (i + 1)
        nc = c1 + dc[2] * (i + 1)

        # 경계 체크
        if 0 <= nr < N and 0 <= nc < N:
            # 값이 1이면 벽. 벽을 만나면 해당 방향 break
            if arr[nr][nc] == 1:
                break # for i
            # 벽이 없으면, 즉 값이 0이면 count -1
            else:
                space_count -= 1

    # 위쪽 보기
    for i in range(N):
        nr = r1 + dr[3] * (i + 1)
        nc = c1 + dc[3] * (i + 1)

        # 경계 체크
        if 0 <= nr < N and 0 <= nc < N:
            # 값이 1이면 벽. 벽을 만나면 해당 방향 break
            if arr[nr][nc] == 1:
                break # for i
            # 벽이 없으면, 즉 값이 0이면 count -1
            else:
                space_count -= 1

    print(f'#{test_case} {space_count}')




















# 출력
# #1 11
# #2 13
# #3 20
# #4 18
# #5 31
