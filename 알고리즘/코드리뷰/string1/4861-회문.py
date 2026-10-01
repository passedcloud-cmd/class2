# import sys
# sys.stdin = open("4861-회문.txt")
# T = int(input())

# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     # N x N 배열 만들기
#     arr = [input() for _ in range(N)]

#     # 테스트 케이스마다 result 초기화
#     result = 0

#     # 가로 기준으로 회문 찾기
#     for r in range(N):
#         for c in range(N - M + 1):
#             word = arr[r][c : c + N]
#             if word == word[::-1]:
#                 result = word
#                 break
#         if result != 0:
#             break

#     # 가로 기준으로 못 찾았으면 세로 기준으로 회문 찾기
#     if result == 0:
#         for c in range(N):
#             for r in range(N - M + 1):
#                 column_word_list = []
#                 for i in range(M):
#                     column_word_list.append(arr[r + i][c])
#                 column_word = "".join(column_word_list)
#                 if column_word == column_word[::-1]:
#                     result = column_word
#                     break #for r
#             if result != 0:
#                 break #for c

#     print(f'#{test_case} {result}')

# 오답노트
# word = arr[r][c : c + N] 로 N짜리 문자열 뽑기

# 문자열 만드는 법 1
# column_word_list = []
# for i in range(M):
#     column_word_list.append(arr[r + i][c])
# column_word = "".join(column_word_list)

# 문자열 만드는 법 2
# vertical_word = ""
# for i in range(M):
#     vertical_word += grid[r + i][c]






##############################다시 풀이
import sys
sys.stdin = open("4861-회문.txt")
T = int(input())
for test_case in range(1, T + 1):
    # N은 배열의 크기를 나타냄. N x N
    # M은 회문의 길이를 나타냄
    N, M = map(int, input().split())
    # N X N array 만들기
    arr = [input() for _ in range(N)]

    # result는 빈값으로 배정하고 시작
    result = "" 

    # 가로에서 회문 찾기
    for row in arr:
        for c in range(N - M + 1):
            word = row[c : M + c]
            if word == word[::-1]:
                result = word
                break # for i
        if result:
            break # for row

    # 가로에서 못 찾았으면 세로에서 회문 찾기
    if not result:
        for c in range(N):
            for r in range(N - M + 1):
                # c가 바뀔 때마다 column_arr 리셋
                column_arr = []

                for i in range(M): 
                    # 세로로 문자열 만들기
                    column_arr.append(arr[r + i][c])

                # 회문이면 break for r
                if column_arr == column_arr[::-1]:
                    # column_arr 가 리스트 형식이니까 하나의 문자열로 만들어주기
                    result = "".join(column_arr)
                    break # for r

            # 회문을 찾았으면 break for c
            if result :
                break # for c
                
    print(f'#{test_case} {result}')

# 오답노트
# 문제의 원인: list(input().split())
# "GOFFAKWFSM".split()을 하면 이렇게 됩니다:
# ['GOFFAKWFSM']   # 통째로 원소 1개짜리 리스트!
# (원소가 1개라 뒤집어도 똑같음!)
# 리스트 안에 원소가 딱 1개밖에 없으면, 그 리스트를 거꾸로 뒤집어도 순서가 바뀔 게 없으니 항상 자기 자신과 같아지는 거예요. 문자열 내용이 회문이든 아니든 상관없이요!

# 입력
# 3
# 10 10
# GOFFAKWFSM
# OYECRSLDLQ
# UJAJQVSYYC
# JAEZNNZEAJ
# WJAKCGSGCF
# QKUDGATDQL
# OKGPFPYRKQ
# TDCXBMQTIO
# UNADRPNETZ
# ZATWDEKDQF
# 10 10
# WPMACSIBIK
# STWASDCOBQ
# AMOUENCSOG
# XTIIGBLRCZ
# WXVSWXYYVU
# CJVAHRZZEM
# NDIEBIIMTX
# UOOGPQCBIW
# OWWATKUEUY
# FTMERSSANL
# 20 13
# ECFQBKSYBBOSZQSFBXKI
# VBOAIDLYEXYMNGLLIOPP
# AIZMTVJBZAWSJEIGAKWB
# CABLQKMRFNBINNZSOGNT
# NQLMHYUMBOCSZWIOBINM
# QJZQPSOMNQELBPLVXNRN
# RHMDWPBHDAMWROUFTPYH
# FNERUGIFZNLJSSATGFHF
# TUIAXPMHFKDLQLNYQBPW
# OPIRADJURRDLTDKZGOGA
# JHYXHBQTLMMHOOOHMMLT
# XXCNJGTXXKUCVOUYNXZR
# RMWTQQFHZUIGCJBASNOX
# CVODFKWMJSGMFTCSLLWO
# EJISQCXLNQHEIXXZSGKG
# KGVFJLNNBTVXJLFXPOZA
# YUNDJDSSOPRVSLLHGKGZ
# OZVTWRYWRFIAIPEYRFFG
# ERAPUWPSHHKSWCTBAPXR
# FIKQJTQDYLGMMWMEGRUZ
#
# 출력
# #1 JAEZNNZEAJ
# #2 MWOIVVIOWM
# #3 TLMMHOOOHMMLT