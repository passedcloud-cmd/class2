import sys
sys.stdin = open('2817_부분수열의_합.txt')

T = int(input())
for test_case in range(1, 1+T):
    # N은 자연수 개수. K는 합해서 되어야 하는 목표 값
    N, K = map(int, input().split())
    # arr은 수열.     # 부분 집합을 합했을 때 K가 되는 경우의 수를 구해야 함
    arr = list(map(int, input().split()))

    def find_sum(idx, subset):
        global cnt # cnt값을 경신할 거라서 전역 변수 선언

        # 가지 치기
        if sum(subset) > K:
            return

        # 종료 조건
        if idx == N: # 모든 자연수를 살펴보았다면
            if sum(subset) == K:
                cnt+=1
            return 

        # 후보군 정하고 탐색
        # 현재 idx 번호를 부분집합에 포함하고 다음으로 넘어가기
        find_sum(idx+1, subset + [arr[idx]])
        # 현재 idx 번호를 포함하지 않고 다음으로 넘어가기
        find_sum(idx+1, subset)

    cnt = 0
    find_sum(0,[]) # 0번째 인덱스, 빈 리스트로 시작
    print(f'#{test_case} {cnt}')

# 1
# 4 3
# 1 2 1 2

# #1 4