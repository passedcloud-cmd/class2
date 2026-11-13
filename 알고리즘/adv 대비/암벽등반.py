import sys
sys.stdin = open('암벽등반.txt')
T = int(input())
for test_case in range(1, T+1):
    # N은 지도의 높이
    # M은 지도의 너비
    N, M = map(int, input().split())
    # 시작점
    start_r, start_c = N-1, 0
    # 지도
    my_map = [list(map(int, input().split())) for _ in range(N)]

    # 목표 지점 찾기
    for i in range(N):
        for j in range(M):
            if my_map[i][j] == 3:
                goal_r, goal_c = i, j

    # 방향키 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # BFS 함수 만들기
    from collections import deque
    def BFS(current_r, current_c, step):
        # 각 지점의 난이도를 나타내는 level 맵 만들기
        level = [[50] * M for _ in range(N)] # 최대 난이도가 50
        # 시작점은 움직이지 않으니까 0
        level[current_r][current_c] = 0
        queue = deque()
        queue.append((current_r, current_c, step))

        while queue:
            r, c, step = queue.popleft()
            # 4방향 
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                # 경계 체크
                if 0 <= nr < N and 0 <= nc < M:
                    # 다음 지점의 레벨이 더 높다면 가보자
                    if level[r][c] < level[nr][nc]:
                        if i <= 1: # 상하 이동이라면
                            level[nr][nc] = max(level[r][c], step+1) # 누적값보다 step+1이 더 크면 경신
                            if my_map[nr][nc] != 0 : # 다음 칸에 발판이 있다면 
                                queue.append((nr,nc,0)) # 발판을 밟으면 step 0으로 초기화
                                continue # 다음 방향으로 가자
                            # 다음 칸에 발판이 없다면
                            queue.append((nr,nc, step+1)) # step+1로 체공 추가
                        else: # 좌우 이동이라면
                            if my_map[r][c] == 0 or my_map[nr][nc] == 0:
                                continue  # 둘 중 하나가 발판이 아니면 이동 못함
                            level[nr][nc] = level[r][c] # 좌우 이동이니까 level은 그대로
                            queue.append((nr,nc,step)) # step도 그대로
        # while문이 끝났다는 건 level 배열이 완성되었다는 뜻
        return level[goal_r][goal_c]

    result = BFS(start_r, start_c, 0) # 시작할 땐 발판이라 step이 0
    print(f'#{test_case} {result}')

    

#1 2
#2 1
#3 3
#4 5
#5 10