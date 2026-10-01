import sys
sys.stdin = open("1989-초심자의회문검사.txt")
T = int(input())

for test_case in range(1, T + 1):
    input_text = input()
    result = 1
    for i in range(len(input_text) // 2):
        if input_text[i] == input_text[-1 - i]:
            result = 1
        else:
            result = 0
            break # for i
    print(f'#{test_case} {result}')



































# # 슬라이싱으로 풀기
# import sys
# sys.stdin = open("1989-초심자의회문검사.txt")
# T = int(input())
# for test_case in range(1, T + 1):
#     words = input()
#     # 회문이면 1
#     if words == words[::-1]:
#         result = 1
#     # 회문이 아니면 0
#     else:
#         result = 0
#
#     print(f'#{test_case} {result}')
#
#
# # 인덱스로 풀기
# import sys
# sys.stdin = open("1989-초심자의회문검사.txt")
# T = int(input())
# for test_case in range(1, T + 1):
#     words = input()
#     N = len(words)
#     # words 길이의 절반만 비교해도 됨
#     for i in range(N // 2):
#         # 회문이 아니면 0을 출력하고 break
#         if words[i] != words[N - 1 - i]:
#             result = 0
#             break
#         # 회문이면 1을 출력
#         else:
#             result = 1
#
#     print(f'#{test_case} {result}')

# 입력
# 3
# level
# samsung
# eye

# 출력
# #1 1
# #2 0
# #3 1