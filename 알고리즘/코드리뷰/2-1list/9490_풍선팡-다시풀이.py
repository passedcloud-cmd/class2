import sys
sys.stdin = open("9490_풍선팡.txt")
T = int(input())

# 방향키 우 좌 상 하 
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    for i in range(N):
        for j in range(M):
            temp_sum = matrix[i][j]

            # dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            # [0, 1]을 돌 때 dx, dy = 0, 1가 됨.
            
            
            for dx, dy in dxy:
                # 각 방향으로 꽃가루 개수만큼 탐색을 해야 함
                for dist in range(1, matrix[i][j] + 1):
                    ni = i + dx * dist
                    nj = j + dy * dist

                    # if 0 <= ni < N and 0 <= nj < M:
                    #     temp_sum += matrix[ni][nj]
                    # # 범위 안에 안 들었을 경우, 해당 방향은 더 이상 안 봐도 됨
                    # else:
                    #     break

                    if 0 > ni or ni >= N or 0 > nj or nj >= M: break

                    temp_sum += matrix[ni][nj]

                max_value = max(max_value, temp_sum)

    print(f'#{test_case} {max_value}')


#1 10
#2 26
#3 40