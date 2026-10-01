import sys
sys.stdin = open("9490_풍선팡.txt")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # N x M 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방향키 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    max_fetal_count = 0
    # arr를 돌면서 합계를 구해야 함
    for r in range(N):
        for c in range(M):
            # 합계가 끝날 때마다 꽃가루 개수 리셋
            fetal_count = 0
            fetal_count += arr[r][c]
            repeat_number = arr[r][c]

            # repeat_number만큼 상하좌우 값 더하기 반복
            for n in range(1, repeat_number + 1):
                # 상하좌우 값 더하기
                for i in range(4):
                    nr = r + dr[i] * n
                    nc = c + dc[i] * n
                    # 경계 체크
                    if 0 <= nr < N and 0 <= nc < M:
                        fetal_count += arr[nr][nc]

            if fetal_count > max_fetal_count:
                max_fetal_count = fetal_count

    print(f'#{test_case} {max_fetal_count}')

# 오답노트
# for문 위치 주의. 언제 최댓값을 갱신할지 생각할 것





































# import sys
# sys.stdin = open("9490_풍선팡.txt")
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#
#     # arr 만들기
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # 방향키 우하좌상
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#
#     max_count = 0 # 최댓값은 임의로 설정
#
#     # 풍선을 터뜨리면 우하좌상 합계 더하기
#     for r in range(N):
#         for c in range(M):
#             # 매번 합계를 기준점으로 초기화하고 시작
#             sum_count = arr[r][c]
#
#             # 우하좌상으로 뻗어나갈 범위도 arr[r][c]
#             fetal_count = arr[r][c]
#
#             # 기준점에 우하좌상 합 계산
#             # fetal_count만큼 반복
#             for i in range(1, fetal_count + 1):
#                 for n in range(4):
#                     nr = r + dr[n] * i
#                     nc = c + dc[n] * i
#
#                     # 경계 체크
#                     if not(0 <= nr < N and 0 <= nc < M):
#                         continue
#
#                     # 합계 누적
#                     sum_count += arr[nr][nc]
#
#             # 최댓값 갱신
#             if sum_count > max_count:
#                 max_count = sum_count
#
#     print(f'#{test_case} {max_count}')


# 4방향 반복 풀이법
# import sys
# sys.stdin = open("9490_풍선팡.txt")

# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     max_count = 0

#     for r in range(N):
#         for c in range(M):
#             V = arr[r][c]      # 이 풍선의 꽃가루 개수 = 터질 개수
#             total = V           # 자기 자신 값부터 시작

#             # 위쪽 방향으로 V개까지 연달아 더하기
#             for i in range(1, V + 1):
#                 nr = r - i
#                 if nr < 0:       # 배열 범위를 벗어나면 멈춤
#                     break
#                 total += arr[nr][c]

#             # 아래쪽 방향으로 V개까지
#             for i in range(1, V + 1):
#                 nr = r + i
#                 if nr >= N:
#                     break
#                 total += arr[nr][c]

#             # 왼쪽 방향으로 V개까지
#             for i in range(1, V + 1):
#                 nc = c - i
#                 if nc < 0:
#                     break
#                 total += arr[r][nc]

#             # 오른쪽 방향으로 V개까지
#             for i in range(1, V + 1):
#                 nc = c + i
#                 if nc >= M:
#                     break
#                 total += arr[r][nc]

#             if total > max_count:
#                 max_count = total

#     print(f'#{test_case} {max_count}')



# 입력
# 3
# 3 5
# 2 1 1 2 2 
# 2 2 1 2 2 
# 2 2 1 1 2 
# 5 5
# 3 4 1 2 3 
# 3 4 1 3 2 
# 2 3 2 4 1 
# 1 4 4 1 3 
# 2 2 3 4 4 
# 5 8
# 1 3 4 4 4 4 3 3 
# 4 1 2 4 3 1 4 4 
# 4 1 4 4 1 4 2 1 
# 3 2 4 2 1 1 2 1 
# 4 4 1 4 4 2 2 2 

# 출력
#1 10
#2 26
#3 40