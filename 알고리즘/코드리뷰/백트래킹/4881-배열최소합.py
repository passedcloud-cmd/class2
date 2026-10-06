import sys
sys.stdin = open('4881-배열최소합.txt')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split)) for _ in range(N)]

