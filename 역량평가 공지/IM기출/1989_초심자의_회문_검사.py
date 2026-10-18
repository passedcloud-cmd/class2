import sys
sys.stdin = open("1989_초심자의_회문_검사.txt")

T= int(input())
for test_case in range(1, T+1):
    # result는 0으로 설정
    result = 0

    text= input()
    text_reverse = text[::-1]
    if text == text_reverse:
        result = 1

    print(f'#{test_case} {result}')

#1 1
#2 0
#3 1