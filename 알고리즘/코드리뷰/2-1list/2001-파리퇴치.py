import sys
sys.stdin = open("2001-파리퇴치.txt")
T = int(input())
for test_case in range(1, T + 1):
    # N은 배열의 크기. M은 파리채의 크키
    N, M = map(int, input().split())
    # N x N arr 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 죽인 파리 수 최댓값 0으로 시작
    max_dead_count = 0

    # r과 c 둘 다 인덱스 [0, N - M + 1]까지 이동하면서 계산.
    for r in range(0, N - M + 1):
        for c in range(0, N - M + 1):
            dead_count = 0  # 파리채를 옮길 때마다 리셋

            # 파리채의 시작점과 끝점이 반복 횟수
            # 시작점은 [r][c]
            # 끝점은 [r + M - 1][c + M - 1]
            for i in range(r, r + M):
                for j in range(c, c + M):
                    dead_count += arr[i][j]
                
            if dead_count > max_dead_count:
                max_dead_count = dead_count

    print(f'#{test_case} {max_dead_count}')

# 오답노트
# 시작점과 끝점을 정하고 그 범위에서 2중 for문
# 방향키 필요 없음
# 범위 주의하기
# [r + M - 1][c + M - 1] 적을 때 오타 주의. c를 r로 적는다든가 하는 실수 있음.
































# import sys
# sys.stdin = open('2001-파리퇴치.txt')
#
# T= int(input())
#
# for test_case in range(1, T + 1):
#     # N은 배열의 크기, M은 파리채의 크기
#     N, M = map(int, input().split())
#
#     # arr 배열을 만듦
#     arr = []
#     for _ in range(N):
#         arr.append(list(map(int, input().split())))
#
#     max_num = arr[0][0] + arr[0][1] + arr[1][0] + arr[1][1] # 최댓값 임의로 정함
#
#     # 더하기 영역에서 시작점-끝점 영역을 찾아서 그 영역 내 값 더하기
#     # N - M + 1 까지만 이동해야 함. 그 밖은 영역 벗어남
#     for r in range(N - M + 1):
#         for c in range(N - M + 1):
#
#             # 한 칸씩 이동할 때마다 M x M 파리채 영역 합을 초기화
#             sum_for_M = 0
#
#             # 시작점과 끝점
#             r1, c1 = r, c
#             r2, c2 = r + M - 1, c + M -1
#
#             # M x M 영역 더하기
#             for i in range(r1, r2 + 1):
#                 for j in range(c1, c2 + 1):
#                     sum_for_M += arr[i][j]
#
#             # 최댓값 구하기
#             if sum_for_M > max_num:
#                 max_num = sum_for_M
#
#     print(f'#{test_case} {max_num}')
    


    





# 입력
# 10
# 5 2
# 1 3 3 6 7
# 8 13 9 12 8
# 4 16 11 12 6
# 2 4 1 23 2
# 9 13 4 7 3
# 6 3
# 29 21 26 9 5 8
# 21 19 8 0 21 19
# 9 24 2 11 4 24
# 19 29 1 0 21 19
# 10 29 6 18 4 3
# 29 11 15 3 3 29

# 출력
# 1 49
# 2 159