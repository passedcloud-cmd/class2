############################### BFS ##############################
import sys
sys.stdin = open('산악구조로봇.txt')
T = int(input())
for test_case in range(1, T+1):
    # N은 지도 크기
    N = int(input())
    # my_map 은 N x N 크기
    my_map = [list(map(int, input().split())) for _ in range(N)]

    INF = float('inf')

    # 방향키 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 연료 소모를 계산하는 함수
    def fuel_consume(current_height, next_height):
        # 높이가 같으면 연료 1 소모
        if current_height == next_height:
            return 1
        # 높이가 낮은 곳으로 갈 땐 연료 소모 없음
        elif current_height > next_height:
            return 0
        # 높이가 높은 곳으로 갈 땐 연료를 높이차 x 2 만큼 소모 
        else:
            return (next_height - current_height) * 2
    
    # BFS 함수 만들기
    from collections import deque
    def BFS(start_r, start_c, arr):
        # 각 지점의 연료를 기록
        fuel = [[INF] * N for _ in range(N)]
        # 시작점 fuel[0][0] = 0
        fuel[0][0] = 0
        queue = deque()
        queue.append([start_r, start_c])
        while queue:
            r, c = queue.popleft()
            # 네 방향 모두 진행
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                # 경계 체크
                if 0 <= nr < N and 0 <= nc < N:
                    # 다음 지점까지 갈 때 소모한 연료 경신
                    re_used = fuel[r][c] + fuel_consume(arr[r][c], arr[nr][nc])
                    # re_sued가 더 저렴하다면 다시 방문
                    if re_used < fuel[nr][nc]:
                        fuel[nr][nc] = re_used
                        # queue에 넣어서 이동
                        queue.append([nr,nc])
        # while문을 끝내고 나면 [N-1][N-1]지점의 연료값 출력
        return fuel[N-1][N-1]
    
    result = BFS(0,0, my_map)
    print(f'#{test_case} {result}')
    

#1 2
#2 16


# ######################## 다익스트라 ###################################
# import sys
# sys.stdin = open('산악구조로봇.txt')
# T = int(input())
# for test_case in range(1, T+1):
#     # N은 지도 크기
#     N = int(input())
#     # my_map 은 N x N 크기
#     my_map = [list(map(int, input().split())) for _ in range(N)]

#     INF = float('inf')

#     # 방향키 상하좌우
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]

#     # 연료 소모를 계산하는 함수
#     def fuel_consume(current_height, next_height):
#         # 높이가 같으면 연료 1 소모
#         if current_height == next_height:
#             return 1
#         # 높이가 낮은 곳으로 갈 땐 연료 소모 없음
#         elif current_height > next_height:
#             return 0
#         # 높이가 높은 곳으로 갈 땐 연료를 높이차 x 2 만큼 소모 
#         else:
#             return (next_height - current_height) * 2
    
#     # 다익스트라 함수 만들기
#     import heapq

#     def daikstra(start_r, start_c, arr):
#         # 각 지점의 연료를 기록
#         fuel = [[INF] * N for _ in range(N)]
#         # 시작점 fuel[0][0] = 0
#         fuel[0][0] = 0

#         # (지금까지 쓴 연료, 행, 열)
#         heap = [(0,start_r,start_c)] # 시작점

#         while heap:
#             used, r, c = heapq.heappop(heap)
#             # 더 적은 연료로 확정된 칸이면 건너뜀
#             if used > fuel[r][c]:
#                 continue

#             # 네 방향 검토
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 # 경계 체크
#                 if 0 <= nr < N and 0 <= nc < N:
#                     used = fuel[r][c] + fuel_consume(arr[r][c], arr[nr][nc])
#                     # 연료 소비가 더 적으면 경신
#                     if used < fuel[nr][nc]:
#                         fuel[nr][nc] = used
#                         heapq.heappush(heap, (used, nr, nc))
#         return fuel[N-1][N-1]

#     result = daikstra(0,0,my_map)
#     print(f'#{test_case} {result}')

# #1 2
# #2 16