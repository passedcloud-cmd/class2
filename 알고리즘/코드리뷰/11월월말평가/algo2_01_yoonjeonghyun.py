import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())
for test_case in range(1, T+1):
    # N은 공장과 물건의 개수
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr) #확인용 출력

    V = [False] * N # 공장별 체크
    min_cost = float('inf') # 구해야 하는 값
    def search(w, cost):
        global min_cost
        # 가지 치기
        # 만약 현재 cost합이 최솟값보다 크면 바로 종료
        if cost > min_cost:
            return

        # 종료 조건
        # 모든 물건을 생산했다면 정산 후 종료
        if w == N:
            if min_cost > cost:
                min_cost = cost
            return

        # 경우의 수 고려
        else:
            for i in range(N): # 모두 돌아가면서 확인
                if not V[i]:  # 해당 공장을 방문하지 않았다면
                    if arr[w][i] != 0: # arr[w][i]값이 0이 아니라면
                        # 경우 1)해당 공장을 선택
                        V[i] = True
                        search(w+1, cost + arr[w][i]) # 해당 공장에서 물건 만들기
                        # 경우 2)해당 공장을 선택하지 않음.
                        V[i] = False

    # 아무 물건도 선택하지 않았고, 그래서 비용이 0인 상태로 시작
    search(0, 0)
    print(f'#{test_case} {min_cost}')

#1 15
#2 5
#3 14


