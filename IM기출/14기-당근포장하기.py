import sys
sys.stdin = open("14기-당근포장하기.txt")
T = int(input())
for test_case in range(1, T + 1):
    # N은 당근 개수
    N = int(input())
    # arr는 당근별 크기
    arr = list(map(int, input().split()))

    # 정렬
    arr_sorted = sorted(arr)

    # 조건1: 대, 중, 소 상자 3개로 나눠서 포장
    # 조건2: 같은 크기는 같은 상자에
    # 조건3: 빈 상자가 있으면 안됨
    # 조건4: 한 상자에 N/2개를 초과해도 안됨. N이 홀수면 소수점 버림
    # 조건5: 각 상자에 든 당근 개수 차이는 최소.
    # 조건을 만족 못하는 경우 -1을 출력

    # 최솟값 설정
    min_diff = float('inf')
    cal_yes = False

    # 가림막 i와 j
    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):

            # 상자별 당근 개수
            # 조건1: 상자 3개.
            # 조건3: 빈 상자 없음
            small_box = i + 1
            middle_box = j - i
            large_box = N - j - 1

            # 조건2: 같은 크기가 다른 상자에 있으면 거르기
            if arr_sorted[i] == arr_sorted[i + 1] or arr_sorted[j] == arr_sorted[j + 1]:
                continue

            # 조건4: 한 상자에 n/2개 초과하면 거르기
            if small_box > N // 2 or middle_box > N // 2 or large_box > N // 2:
                continue

            # 당근 개수 차이 구하기
            diff = max(small_box, middle_box, large_box) - min(small_box, middle_box, large_box)
            # 최솟값 갱신
            min_diff = min(diff, min_diff)
            cal_yes = True
    if cal_yes:
        result = min_diff
    else:
        result = -1

    print(f'#{test_case} {result}')


# 입력
# 8
# 3
# 1 2 3
# 5
# 1 1 1 2 3
# 8
# 1 2 3 4 5 6 7 8
# 5
# 1 2 2 3 4
# 10
# 1 2 3 3 3 4 5 6 7 8
# 9
# 1 1 1 1 2 3 3 3 3
# 9
# 1 1 1 2 2 2 3 3 3
# 9
# 1 1 1 1 2 2 30 30 30 30 2

# 출력
# #1 0
# #2 -1
# #3 1
# #4 1
# #5 2
# #6 3
# #7 0
# #8 2