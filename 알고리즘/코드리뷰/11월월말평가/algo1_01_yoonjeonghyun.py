import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())
for test_case in range(1, T+1):
    # M은 전구의 개수
    M = int(input())

    k = 0 # 층수 0으로 시작
    while M > k:
        k += 1 # 하나 반복 할 때마다 필요한 전구 개수 1개씩 증가, 층 수도 +1
        M -= k # 남은 개수 M에서 k만큼 빼기

    # N은 최대 층수
    N = k

    print(f'#{test_case} {N}')



# def need_number(k):
#     """k층을 만들기 위해 필요한 전구 개수"""
#     global result
#     result = (k*(k+1) / 2)
#     return result
# # need_number(k) <= M이어야 함.
# need_number(315)
# print(result)

#1 1
#2 4
#3 5
