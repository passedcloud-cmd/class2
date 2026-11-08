import sys
sys.stdin = open("29948_자연수의합.txt")
T = int(input())
for test_case in range(1, T+1):
    # M은 합의 최솟값
    M = int(input())
    
    S = 0 # 합은 0에서 시작
    increase_num = 0 # 1씩 증가하는 자연수
    while not (S >= M):
        increase_num += 1
        S += increase_num

    N = increase_num
    print(f'#{test_case} {N}')


############################
##### 다른 풀이 방법 #########
    def prefix_sum(n):
        return n * (n+1) // 2

    # 답은 1 ~ M 사이에 있음
    low, high = 1, M # 정답의 범위

    # low = high가 될 때의 값이 정답
    while low < high:
        mid = (low + high) // 2
        if prefix_sum(mid) >= M:
            high = mid
        else:
            low = mid +1

    print(f'#{test_case} {low}')
    print(f'#{test_case} {high}')



#1 1
#2 4
#3 141