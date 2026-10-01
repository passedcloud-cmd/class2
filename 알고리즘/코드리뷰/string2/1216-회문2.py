import sys
sys.stdin = open("input.txt")






































# import sys
# sys.stdin = open("1216-회문2.txt")
# T = 10
# for test_csae in range(1, T + 1):
#     # N은 테스트 케이스 번호
#     N = int(input())
#     # 100 X 100 arr 만들기
#     arr = [input() for _ in range(100)]
#     arr_T = list(map("".join, zip(*arr)))
#
#     result_length = ""
#     # 회문 길이
#     for length in range(100, 0, -1):
#         # row 100개 훑기
#         for r in range(100):
#             # 시작점 j
#             for j in range(0, 100 - length + 1):
#                 # 가로
#                 if arr[r][j: j + length] == arr[r][j: j + length][::-1]:
#                     result_length = length
#                     break # for j
#                 # 세로
#                 elif arr_T[r][j: j + length] == arr_T[r][j: j + length][::-1]:
#                     result_length = length
#                     break # for j
#
#             if result_length:
#                 break # for r
#         if result_length:
#             break # for length
#
#     print(f'#{test_csae} {result_length}')



# 출력
# #1 1
# #2 100
# #3 100
# #4 8
# #5 18
# #6 21
# #7 18
# #8 18
# #9 17
# #10 18