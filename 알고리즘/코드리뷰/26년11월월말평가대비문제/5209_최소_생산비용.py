import sys
sys.stdin = open("5209_최소_생산비용.txt")
T = int(input())
for test_case in range(1, T+1):
    # 제품의 수 N
    N = int(input())
    # 공장별 생산 비용
    V = [list(map(int, input().split())) for _ in range(N)]

# ######################################
# ######### 순열 확인 ###################
#     visited = [0] * N # 제품별로 경우의 수 확인 
#     picked = []

#     def search_choice(w):
#         # 종료 조건
#         # 모든 물품을 골랐다면
#         if w == N:
#             print(picked)
#             return 

#         # 다른 물품 비용 더하기
#         for i in range(N):
#             # 이전에 더하지 않은 상품이면
#             if not visited[i]:
#                 # 경우1- 해당 상품 넣기
#                 visited[i] = 1
#                 picked.append(i)
#                 search_choice(w + 1)
#                 # 경우2- 해당 상품 안 넣기. 이전 상태로 되돌리기
#                 picked.pop()
#                 visited[i] = 0

#     search_choice(0)


    visited = [0] * N # 공장별로 경우의 수 확인 
    min_sum = float('inf')

    def search(w, cost):
        global min_sum
        # 가지 치기
        if cost > min_sum:
            return

        # 종료 조건
        # 모든 물품을 골랐다면
        if w == N:
            if cost < min_sum:
                min_sum = cost

        else:
            # 다른 물품 비용 더하기
            for i in range(N):
                # 이전에 더하지 않은 상품이면
                if not visited[i]:
                    # 경우1- 해당 상품 넣기
                    visited[i] = 1
                    search(w + 1, cost + V[w][i])
                    # 경우2- 해당 상품 안 넣기. 이전 상태로 되돌리기
                    visited[i] = 0

    # 아무 공장도 선택하지 않고, 그래서 비용이 0인 상태에서 시작.
    search(0, 0)
    print(f'#{test_case} {min_sum}')




# #1 63
# #2 78
# #3 129

