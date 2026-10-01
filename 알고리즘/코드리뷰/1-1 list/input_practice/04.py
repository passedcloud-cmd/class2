import sys

sys.stdin = open('04.txt')

T = int(input())

for tc in range(1, T + 1):
    matrix = []
    N = int(input())

    # 1
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    # 2
    # matrix = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}')
    print(f'{matrix}')

# 첫 번째 테스트 케이스 3번 반복하고 그 안에서 또 테스트 케이스 반복