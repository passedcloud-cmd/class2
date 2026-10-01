import sys
sys.stdin = open("1215-회문1.txt")
T = 10
for test_case in range(1, T + 1):
    # N은 찾아야 하는 회문의 길이
    N = int(input())
    arr = [input() for _ in range(8)]

    count_palindrome = 0
    # 가로 방향으로 찾기
    for row in arr:
        for r in range(0, 8 - N + 1):
            # 회문인지 확인할 문자열 만들기
            arr_make = []
            for i in range(N):
                arr_make.append((row[r + i]))
            # 회문인지 체크
            if arr_make == arr_make[::-1]:
                count_palindrome += 1

    arr_T = list(map("".join, zip(*arr)))
    # row 8개 돌기
    for r in range(8):
        # 시작점 c는 0 ~ (뒤에서 N을 뺀 값)
        for c in range(0, 8 - N + 1):
            if arr_T[r][c:c+N] == arr_T[r][c:c+N][::-1]:
                count_palindrome += 1

    print(f'#{test_case} {count_palindrome}')



    # # 세로 방향으로 찾기
    # for c in range(8):
    #     for r in range(0, 8 - N + 1):
    #         # 회문인지 확인할 문자열 만들기
    #         arr_make = []
    #         for i in range(N):
    #             arr_make.append(arr[r + i][c])
    #         # 회문인지 체크
    #         if arr_make == arr_make[::-1]:
    #             count_palindrome += 1

    # print(f'#{test_case} {count_palindrome}')