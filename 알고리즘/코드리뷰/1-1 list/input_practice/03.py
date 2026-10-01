import sys

sys.stdin = open('03.txt')

N = int(input()) #3

# 1
number_list = []
for _ in range(N):
    row = list(map(int, input().split()))
    number_list.append(row) #2차원 행렬로 만듦

# 2
# number_list = [list(map(int, input().split())) for _ in range(N)] #1번과 결과 똑같음

print(number_list)
