import sys
sys.stdin = open("2001-파리퇴치.txt")
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    kill_flies = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp_sum = 0
            # print(f'i:{i}, j:{j}')
            for m in range(M):
                for n in range(M):
                    # print(m, n)
                    # print(i + m, j + n)
                    temp_sum += matrix[i + m][j + n]
            kill_flies = max(kill_flies, temp_sum)

    print(f'#{tc} {kill_flies}')

#1 49
#2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242