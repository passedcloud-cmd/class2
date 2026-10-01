import sys
sys.stdin = open("5099_피자굽기.txt")
T = int(input())

from collections import deque

for test_case in range(1, T + 1):
    # N은 한번에 넣을 수 있는 피자 개수
    # M은 만들어야 하는 피자 개수
    N, M = map(int, input().split())

    cheese_list = [(i, val) for i, val in enumerate(map(int, input().split()), 1)]
    print(cheese_list)


    # 오븐 채우기
    oven = []
    for _ in range(N):
        oven.append(cheese_list.pop(0))

    while len(oven) > 1 :
        pizza, val = oven.pop(0)
        val = val // 2

        if val > 0:
            oven.append([pizza, val])
        elif val == 0 and cheese_list:

            oven.append(cheese_list.pop(0))

    last_pizza = oven[0][0]
    print(last_pizza)
    




















#1 4
#2 8
#3 6