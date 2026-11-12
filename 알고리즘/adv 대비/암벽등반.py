import sys
sys.stdin = open('암벽등반.txt')

from collections import deque
T = int(input())
for test_case in range(1, T+1):
    # N은 암벽 지도의 높이. M은 너비
    N, M = map(int, input().split())
    start_N, start_M = N - 1, 0



















#1 2
#2 1
#3 3
#4 5
#5 10