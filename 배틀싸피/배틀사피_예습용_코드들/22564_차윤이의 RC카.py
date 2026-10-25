import sys
sys.stdin = open('22564_차윤이의 RC카.txt')

# 상 우 하 좌(시계방향)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for test_case in range(1, 1+T):
    # 필드의 크기 N
    N = int(input())
    grid = [list(map(str, input())) for _ in range(N)]

    # 전차 시작 위치X와 목적지 Y찾기
    start_r, start_c = 0,0
    end_r, end_c =0,0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'X':
                start_r, start_c = i,j
            elif grid[i][j] == 'Y':
                end_r, end_c = i, j
    

    # 조종횟수 Q
    Q = int(input())
    results = []
    for _ in range(Q):
        line = input().split()
        commands = line[1] # 커맨드 길이
        # 매 커맨드마다 초기 상태에서 시작
        cur_r, cur_c = start_r, start_c
        direction = 0 # 항상 위를 바라보고 시작

        for cmd in commands:
            if cmd == 'L':
                # 왼쪽 90도 회전
                direction = (direction -1) % 4 # 파이썬은 나누는 숫자의 부호를 따라서 나머지 값이 나옴 
            elif cmd == 'R':
                # 오른쪽으로 90도 회전
                direction = (direction +1)% 4
            else:
                # 'A': 앞으로 한 칸 이동 시도
                nr = cur_r + dr[direction]
                nc = cur_c + dc[direction]
                # 맵 안이고 나무(T)가 아닌 경우만 이동
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 'T':
                    cur_r, cur_c = nr, nc

        # 커맨드 종료 후 목적지에 있는지 확인
        if cur_r == end_r and cur_c == end_c:
            results.append('1')
        else:
            results.append('0')

    print(f'#{test_case}', ' '.join(results))




#1 1 0 1