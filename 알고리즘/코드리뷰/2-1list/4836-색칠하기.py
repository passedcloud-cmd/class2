import sys
sys.stdin = open("4836-색칠하기.txt")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    purple_count = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                arr[r][c] += color

    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                purple_count += 1


    print(f'#{test_case} {purple_count}')


































# import sys

# sys.stdin = open("4836-색칠하기.txt")

# 칸이 칠해졌는지 무슨색인지 고려하는 방법1
# T = int(input())
# for t in range(T):
#     purple_count = 0

#     # 임의로 (10, 10) 행렬 만듦
#     arr = list([0] * 10 for _ in range(10)) 

#     # N = 색을 칠할 영역
#     N = int(input()) 
#     for i in range(N):
#         r1, c1, r2, c2, color = map(int, input().split())

#         # 순회하기
#         for r in range(r1, r2 + 1):
#             for c in range(c1, c2 + 1):
#                 # case1: 칸이 빈칸도 아니고 같은 색도 아님 -> 다른 색이 칠해짐
#                 if arr[r][c] != 0 and arr[r][c] != color:
#                     # 그리고 보라색이 아님 
#                     if arr[r][c] != 3:
#                         purple_count += 1
#                         arr[r][c] =3
#                 # case2: 그 외의 경우 - 빈칸이거나 같은 색이면
#                 else:
#                     arr[r][c] = color #색을 칠해버림 

#     print(f'#{t+1} {purple_count}')


###################################################################

# import sys

# sys.stdin = open("4836-색칠하기.txt")
# 안 보고 다시 시작
# T = int(input())

# for t in range(T):
# 	# 임의로 값이 0인 행렬 10x10을 만듦
#     arr = [[0] * 10 for _ in range(10)]
    
#     # 보라색 칸의 개수는 처음에 0
#     purple_count = 0
    
#     # 색을 칠할 영역의 개수 N
#     N = int(input())
#     for _ in range(N):
#         # 색칠 영역의 시작점과 끝점 정하기
#         r1, c1, r2, c2, color = map(int, input().split())
    	
#         # 색 칠하기
#         for r in range(r1, r2 + 1): # 행 중심으로 순회
#             for c in range(c1, c2 +1):
                
#                 # 칸이 0이거나 같은 색이면 같은색으로 칠하기
#                 if arr[r][c] == 0 or arr[r][c] == color:
#                     arr[r][c] = color
#                 # 칸이 0이 아니고 다른 색인 경우
#                 else:
#                     # # 칸이 이미 보라색이라면 그냥 넘어가기
#                     # if arr[r][c] == 3:
#                     #     continue
#                     # # 칸이 다른 색이라면 보라색으로 만들고 보라색 개수 +1
#                     # else:
#                         arr[r][c] = 3
#                         purple_count +=1
                           
#     print(f'#{t+1} {purple_count}')
###################################################################

# import sys
#
# sys.stdin = open("4836-색칠하기.txt")
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     # N은 색칠할 영역의 개수
#     N = int(input())
#
#     # 0으로 채워진 10 x 10 배열
#     arr = [[0] * 10 for _ in range(10)]
#
#     # 영역의 개수만큼 반복
#     for _ in range(N):
#         # 시작점 (r1, c1)과 (r2, c2)와 color에 값 할당
#         r1, c1, r2, c2, color = map(int, input().split())
#
#         # 색칠할 영역 내에서 완전탐색 하면서 색깔 숫자 더하기
#         for r in range(r1, r2 + 1):
#             for c in range(c1, c2 + 1):
#                 arr[r][c] += color
#
#     # 색깔 숫자가 3인 영역 찾기
#     purple_count = 0
#     for r in range(10):
#         for c in range(10):
#             if arr[r][c] == 3:
#                 purple_count += 1
#
#     print(f'#{test_case} {purple_count}')

# 정답 예시
#1 4
#2 5
#3 7

# 입력 예시
# 3
# 2
# 2 2 4 4 1
# 3 3 6 6 2
# 3
# 1 2 3 3 1
# 3 6 6 8 1
# 2 3 5 6 2
# 3
# 1 4 8 5 1
# 1 8 3 9 1
# 3 2 5 8 2