import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for test_case in range(1, 4):
    # N은 map 크기
    N = int(input())
    # arr은 N x N 크기
    arr = [list(map(int, input().split())) for n in range(N)]
    # 확인용 출력
    # print(arr)

    # 일단 bfs를 구현해보자
    from collections import deque
    def bfs(start):
        visited = [[False] * N for _ in range(N)]
        path =[]
        queue = deque()
        queue.append(start)

        while queue:
            r, c = queue.popleft()
            path.append((r, c))
            for i







#1 2
#2 16
#3 32
#4 66
#5 93