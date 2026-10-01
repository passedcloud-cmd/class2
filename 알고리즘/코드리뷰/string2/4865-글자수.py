import sys
sys.stdin = open("4865-글자수.txt")
T = int(input())

def most_frequency_str(input_str1, input_str2):
    # input_str1 길이
    N = len(input_str1)
    # input_str2의 길이
    M = len(input_str2)

    # cnt 최댓값은 0으로 시작
    cnt_max = 0

    for i in range(N):
        cnt = 0 # str2 한 번 돌면 cnt 초기화
        for j in range(M):
            if input_str1[i] == input_str2[j]:
                cnt += 1
        # 최댓값 갱신
        if cnt > cnt_max:
            cnt_max = cnt

    return cnt_max


for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    print(f'#{test_case} {most_frequency_str(str1, str2)}')




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
# #1 2
# #2 1
# #3 3