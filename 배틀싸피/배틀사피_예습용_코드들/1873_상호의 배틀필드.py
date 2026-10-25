import sys
sys.stdin = open('1873_상호의 배틀필드.txt')
T = int(input())

# 상하좌우
dr = [-1, 1, 0, 0] 
dc = [0, 0, -1, 1]
# 각 방향에 대응하는 전차 모양
tank_shape = ['^', 'v', '<', '>']
# 명령어 - 방향 매핑
cmd_to_dir = {'U': 0, 'D': 1, 'L':2, 'R':3}

for test_case in range(1, 1+T):
    # H, W는 높이와 너비
    H, W = map(int, input().split())
    grid = [list(map(str, input())) for _ in range(H)]
    # print(grid) # 확인용 출력
    # N은 명령어 숫자
    N = int(input())
    commands = input()
    # print(command) # 확인용 출력

    # 전차 초기 위치와 방향 찾기
    tank_r, tank_c, tank_dir = 0,0,0
    for i in range(H):
        for j in range(W):
            if grid[i][j] in tank_shape:
                tank_r, tank_c = i, j
                tank_dir = tank_shape.index(grid[i][j]) # .index()는 어떤 값이 몇 번째 자리에 있는지 알려주는 함수

    # 명령어를 하나씩 처리
    for cmd in commands:
        if cmd in cmd_to_dir: #cmd_to_dir = {'U': 0, 'D': 1, 'L':2, 'R':3}
            # -----이동 명령------
            tank_dir = cmd_to_dir[cmd] #숫자
            # 전차 모양 갱신
            grid[tank_r][tank_c] = tank_shape[tank_dir]
            # 이동할 다음 좌표
            nr = tank_r + dr[tank_dir]
            nc = tank_c + dc[tank_dir]
            # 맵 안이고 평지('.')일 때만 이동
            if 0 <= nr < H and 0 <= nc <W and grid[nr][nc] == '.':
                grid[tank_r][tank_c] = '.' # 원래 자리는 평지가 됨
                tank_r, tank_c = nr, nc
                grid[tank_r][tank_c] = tank_shape[tank_dir] # 새로운 자리에 전차가 이동

        else: # -------발사 명령-------
            # 포탄은 전차 위치에서 현재 방향으로 한 칸씩 전진
            br, bc = tank_r + dr[tank_dir], tank_c + dc[tank_dir]
            # 맵 밖으로 나갈 때까지 반복
            while 0 <= br < H and 0 <= bc < W:
                if grid[br][bc] == '*': # 벽돌벽
                    grid[br][bc] = '.' #벽돌벽 파괴해서 평지됨
                    break # 포탄은 사라짐
                elif grid[br][bc] == '#': # 강철벽
                    break # 아무일 없이 포탄 소멸
                # 평지나 물이면 계속 직진
                br += dr[tank_dir]
                bc += dc[tank_dir]

    print(f'#{test_case}', end=' ')
    for row in grid:
        print(''.join(row))


    

# #1 *....*
# ......
# ..-...
# ..>#..
# #2 <.
# ..
# #3 ^-#**
# .-.#*
# .-..#
# #4 .....
# .***.
# ..*..
# ..*..
# ....v
# #5 ###
# #>#
# ###
# #6 ###
# #<#
# ###
# #7 ###
# #^#
# ###
# #8 ###
# #v#
# ###
