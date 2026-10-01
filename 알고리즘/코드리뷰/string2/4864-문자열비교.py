import sys
sys.stdin = open("4864-문자열비교.txt")
T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)

    # 같은 글자 수
    cnt = 0

    result = 0 # 임의로 설정

    # 더 긴 문자열 str2를 훑기
    for i in range(M - N + 1):
        for j in range(N):
            # 두 글자가 같으면 nt += 1
            if str2[i + j] == str1[j]:
                cnt += 1
            # 두 글자가 같지 않으면 초기화
            else:
                cnt = 0
                break # for j
        # cnt == N이면 str2에 str1이 포함된 것
        if cnt == N:
            result = 1
            break # for i

    print(f'#{test_case} {result}')







# 입력
# 3
# XYPV
# EOGGXYPVSY
# STJJ
# HOFSTJPVPP
# ZYJZXZTIBSDG
# TTXGZYJZXZTIBSDGWQLW
#
# 출력
# #1 1
# #2 0
# #3 1