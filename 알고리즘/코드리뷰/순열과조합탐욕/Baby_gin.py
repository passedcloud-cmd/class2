# ## 순열
# import sys
# sys.stdin = open('Baby_gin.txt')

# def find_run(arr):
#     return arr[2] == arr[1] + 1 and arr[1] == arr[0] + 1

# def find_triplet(arr):  
#     return arr[2] == arr[1] == arr[0]

# T = int(input())
# for test_case in range(1, T+1):
#     cards = list(map(int, input()))
#     result = 0

#     import itertools
#     cards_list = list(itertools.permutations(cards))

#     for per in cards_list:
#         left = per[0:3]
#         right = per[3:]


#         if (find_run(left) or find_triplet(left)) and (find_run(right) or find_triplet(right)):
#             result = 1
#             break # for per

#     print(f'#{test_case} {result}')



        

## 조합
import sys
sys.stdin = open('Baby_gin.txt')

def find_run(arr):
    arr.sort()
    return arr[2] == arr[1] + 1 and arr[1] == arr[0] + 1

def find_triplet(arr):  
    return arr[2] == arr[1] == arr[0]

T = int(input())
for test_case in range(1, T+1):
    cards = list(map(int, input()))
    result = 0 # 결과값은 0으로 시작

    import itertools
    # 인덱스 0~5 중 3개를 무작위로 골라서(조합) 카드를 첫번째 3가지와 나머지 3가지로 나누기
    for group1_indices in itertools.combinations(range(6), 3):
        group1 = [cards[i] for i in group1_indices]
        group2_indices = list(set(range(6)) - set(group1_indices))
        # set(range(6)) = {0, 1, 2, 3, 4, 5}
        # list의 경우 +로 더하기는 되지만 -로 덜어내기는 못함
        # set의 경우에만 차집합처럼 -로 덜어내기 가능
        # group2_indices = [i for i in range(6) if i not in group1_indices]로 쓰기 가능(리스트 컴프리헨션)
        group2 = [cards[i] for i in group2_indices]

        # 첫 번째 카드 조합과 두 번째 카드 조합에서 run이나 triplet이 1번씩 일어나면 baby-gin
        if (find_run(group1) or find_triplet(group1)) or (find_run(group2) or find_triplet(group2)):
            result = 1
            break # for group1_indices
    
    print(f'#{test_case} {result}')






#1 1
#2 1
#3 0
#4 1
#5 1
#6 1
#7 1
#8 1
#9 0