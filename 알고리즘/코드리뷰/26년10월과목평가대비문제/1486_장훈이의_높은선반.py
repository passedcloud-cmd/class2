import sys
sys.stdin = open('1486_장훈이의_높은선반.txt')

T = int(input())
for test_case in range(1, T+1):
    # N은 정수의 개수, B는 만들어야 하는 탑 최소 높이
    N, B = map(int, input().split()) # 5, 16
    people = list(map(int, input().split()))

    def make_top(k, subset):
        global min_top
        # 가지치기 없음

        # 기저 조건
        if k == N:
            if sum(subset) >= B:
                min_top = min(min_top, sum(subset))
            return

        # 후보군 정하고 탐색
        make_top(k+1, subset + [people[k]])
        make_top(k+1, subset)

    min_top = float('inf')
    make_top(0, [])
    ans = min_top - B
    print(f'#{test_case} {ans}')

## 입력
# 1
# 5 16
# 1 3 3 5 6
## 출력
# #1 1