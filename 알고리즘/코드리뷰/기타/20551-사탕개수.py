import sys
sys.stdin = open("20551.txt")

T = int(input())
for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())

    # 먹은 개수
    cnt = 0

    # 각 상자마다 최소개수 못 채우면 -1 출력
    if A < 1 or B < 2 or C < 3:
        result = -1
        print(f'#{test_case} {result}')
        continue

    while B >= C :
        B -= 1
        cnt += 1

    while A >= B :
        A -= 1
        cnt += 1

    result = cnt

    print(f'#{test_case} {result}')




# 4
# 3 2 1
# 1 2 3
# 3 5 5
# 5 6 6

#1 -1
#2 0
#3 1
#4 2