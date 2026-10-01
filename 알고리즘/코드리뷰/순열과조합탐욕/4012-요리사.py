import sys
sys.stdin = open("4012-요리사.txt")

T = int(input())
for test_case in range(1):
    # N은 식재료 개수
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for row in arr:
        print(row)

    import itertools
    indices = list(range(N)) # [0, 1, 2, 3]

    food1_indices = list(itertools.combinations(indices, 2)) # [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    for i, j in food1_indices:
        S1_ij = arr[i][j]
        S1_ji = arr[j][i]
        S1 = S1_ij + S1_ji

        #food2의 인덱스 찾기
        food2_indices = set(range(5)) - set(f)





#1 2
#2 1
#3 38
#4 15
#5 4
#6 0
#7 51
#8 23
#9 13
#10 11 