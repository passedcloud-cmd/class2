# import sys
# sys.stdin = open('5215_햄버거_다이어트.txt')


### 조합 꺼내서 풀었더니 런타임 아웃남
# T = int(input())
# for test_case in range(1, T+1):
#     # N은 재료의 수. L은 제한 칼로리
#     N, L = map(int, input().split())
#     #맛에 대한 점수 T와 칼로리K
#     arr_TK = [list(map(int, input().split())) for _ in range(N)]
#     # print(arr_TK)

#     # 조합 함수 구현
#     def combination(arr, r):
#         if r == 0:
#             return [[]]
#         result = []
#         for i in range(len(arr)):
#             elem = arr[i]
#             next_arr = arr[i+1:]
#             for rest in combination(next_arr, r-1):
#                 result.append(rest+[elem])
#         return result

#     best_taste = 0
#     for i in range(1, N+1):
#         for combo in combination(arr_TK, i):
#             taste = 0
#             cal = 0
#             # print(combo)

#             for t, k in combo:
#                 taste += t
#                 cal += k
#             if cal <= L:
#                 best_taste = max(best_taste, taste)

#     print(f'#{test_case} {best_taste}')




# import sys
# sys.stdin = open('5215_햄버거_다이어트.txt')

# T = int(input())
# for test_case in range(1, T+1):
#     # N은 재료의 수. L은 제한 칼로리
#     N, L = map(int, input().split())
#     #맛에 대한 점수 T와 칼로리K
#     arr_TK = [list(map(int, input().split())) for _ in range(N)]
#     # print(arr_TK)

#     def find_best_taste(idx, cal, taste):
#         global best_taste

#         # 가지 치기
#         if cal > L:
#             return
#         # 종료 조건
#         if idx == N:
#             best_taste = max(best_taste, taste)
#             return

#         t, k = arr_TK[idx]

#         # 현재 재료를 추가하는 경우
#         find_best_taste(idx+1, cal+k, taste+t) 
#         # 현재 재료를 추가하지 않는 경우
#         find_best_taste(idx+1, cal, taste)

#     best_taste = 0
#     find_best_taste(0,0,0)
#     print(f'#{test_case} {best_taste}')



# 입력
# 1
# 5 1000
# 100 200
# 300 500
# 250 300
# 500 1000
# 400 400

#출력
#1 750