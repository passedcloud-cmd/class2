import sys
sys.stdin = open('1209_sum.txt')
T = 10
for test_case in range(1, T+1):
    # N은 테스트 케이스 번호
    N = int(input())
    # arr는 100x100 배열
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 최댓값 0부터 시작
    max_sum = float('-inf')

    # 행의 합
    # 행 하나 고정하고
    for i in range(100):
        # 열 하나씩 이동하면서 각 행의 합 구하기
        tmp_sum = 0
        for j in range(100):
            tmp_sum += arr[i][j]
        # 최댓값 경신
        max_sum = max(max_sum, tmp_sum)

    # 열의 합
    # 열 하나 고정하고
    for j in range(100):
        # 행 하나씩 이동하면서 긱 열의 합 구하기
        tmp_sum = 0
        for i in range(100):
            tmp_sum += arr[i][j]
        # 최댓값 경신
        max_sum = max(max_sum, tmp_sum)

    # 각 대각선의 합
    tmp_sum1 = 0
    tmp_sum2 = 0
    for i in range(100):
        tmp_sum1 += arr[i][i]
        tmp_sum2 += arr[i][-i-1]
    # 최댓값 경신
    max_sum = max(max_sum, tmp_sum1, tmp_sum2)

    print(f'#{test_case} {max_sum}')


#1 1712
#2 1743
#3 1713
#4 1682
#5 1715
#6 1730
#7 1703
#8 1714
#9 1727
#10 1731
