import sys
sys.stdin = open("5209_최소_생산비용.txt")
T = int(input())
for test_case in range(1, 2):
    # 제품의 수 N
    N = int(input())
    # 공장별 생산 비용
    V = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N # 경우의 수 확인 
    picked = []

    def search(w):

        # 종료 조건
        if w == N:
            print(picked)
            return 


        # 다른 물품 비용 더하기
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                picked.append(i)
                search(w + 1)
                picked.pop()
                visited[i] = 0


    search(0)




# #1 63
# #2 78
# #3 129

