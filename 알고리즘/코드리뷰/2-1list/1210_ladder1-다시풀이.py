# 위에서 아래로.
# import sys
# sys.stdin = open('1210_ladder1.txt')

# # 마지막 숫자가 2이면 True, 아니면 False
# def search_ladder(x, y):
#     # 원본을 훼손하지 않기 위해서 복사본을 만들자
#     visited = [[0] * N for _ in range(N)]
#     visited[x][y] = 1 # 이미 방문했다면 1로 바꾸기


#     dxy = [[1, 0], [0, -1], [0, 1]]
#     # 이제 아래, 왼, 오른으로 반복
#     while x != 99:
#         for dx, dy in dxy:
#             nx, ny = x + dx, y + dy

#             # 이동 조건
#             # 1. 범위 벗어나면 안됨
#             if nx < 0 or nx >= N or ny < 0 or ny >= N: continue

#             # 2. 사다리가 놓여있어야 함
#             if not data[nx][ny] : continue

#             # 3. 이미 방문한 경우에는 안됨
#             if visited[nx][ny]: continue

#             # 여기까지 코드가 도착했다면
#             visited[nx][ny] = 1

#             x, y = nx, ny

#     return data[x][y] == 2

# for _ in range(1, 11):
#     tc = int(input())
#     N = 100

#     # 사다리타기 -> 마지막에 도달했을 때 2가 되는 시작지점을 찾기
#     result = -1 # 임의 설정
#     data = [list(map(int, input().split())) for _ in range(N)]

#     # 모든 출발점에서 다 시작해보고, 마지막이 2인 곳을 반환
#     for j in range(N):
#         if data[0][j] == 1: #1인 부분에서 사다리 탐색 시작
#             if search_ladder(0, j): # 도착지점이 2이면 True, 아니면 False
#                 result = j
#                 break # for j

#     print(f'#{tc} {result}')


#아래에서 위로.
import sys
sys.stdin = open('1210_ladder1.txt')

# 마지막 숫자가 2이면 True, 아니면 False
def search_ladder(x, y):
    # 복사본 필요 없음. 원본을 수정하면서 올라가도 됨

    data[x][y]= 0
    #우 좌 상
    dxy = [[0, 1], [0, -1], [-1, 0]]

    while x != 0:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 이동 조건
            # 1. 범위 벗어나면 안됨
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue

            # 2. 사다리가 놓여있어야 함
            if not data[nx][ny] : continue

            # 여기까지 코드가 도착했다면 나아가도 됨.
            data[nx][ny] = 0 # 다음 지점을 0으로 만들고

            # 나아가기
            x, y = nx, ny
    # x = 0에 도달
    return y

for _ in range(1, 11):
    tc = int(input())
    N = 100

    # 사다리타기 -> 마지막에 도달했을 때 2가 되는 시작지점을 찾기
    result = -1 # 임의 설정
    data = [list(map(int, input().split())) for _ in range(N)]

    # 도착점에서 아예 거꾸로 올라가자
    for j in range(N):
        if data[99][j] == 2:
            result = search_ladder(99, j)
            break

    print(f"#{tc} {result}")