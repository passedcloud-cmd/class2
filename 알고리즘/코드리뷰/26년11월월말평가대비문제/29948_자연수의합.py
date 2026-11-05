import sys
sys.stdin = open("29948_자연수의합.txt")
T = int(input())
for test_case in range(1, T+1):
    # M은 합의 최솟값
    M = int(input())
    
    # S = 0 # 합은 0에서 시작
    # tmp_num = 0
    # while not (S >= M):
    #     tmp_num += 1
    #     S += tmp_num

    # M = tmp_num
    # print(f'#{test_case} {M}')



    def prefix_sum(n):
        return n * (n+1) // 2

    low, high = 1, M

    while low < high:
        mid = (low + high) //2
        if prefix_sum(mid) >= M:
            high = mid
        else:
            low = mid +1

    print(f'#{test_case} {low}')




#1 1
#2 4
#3 141