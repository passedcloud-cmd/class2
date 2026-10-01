# 딕셔너리 사용

import sys
sys.stdin = open("4834-숫자카드.txt")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    # {'숫자': '카드 장수'} 딕셔너리 만들기
    arr_dict = {}
    for i in arr:
        # 딕셔너리에 해당 숫자가 없으면 해당 숫자 추가하고 count +1
        if i not in arr_dict:
            arr_dict[i] = 1
        # 딕셔너리에 해당 숫자가 있으면 count +1
        else:
            arr_dict[i] += 1

    # 가장 많이 나온 숫자와 카드 장수를 0으로 임의 할당
    most_frequent_number = 0
    number_count = 0

    for key, value in arr_dict.items():
        # 카드 장수가 가장 많은 숫자인 경우
        if value > number_count:
            number_count = value
            most_frequent_number = key

        # 카드 장수가 같은 경우
        elif value == number_count:
            # 적힌 숫자가 더 큰 쪽을 선택
            if key > most_frequent_number:
                number_count = value
                most_frequent_number = key

    print(f'#{test_case} {most_frequent_number} {number_count}')







# import sys
#
# sys.stdin = open("4834-숫자카드.txt")
#
# T = int(input()) #5
#
# for t in range(T):
#     N = int(input())
#     arr = list(map(int, input())) # 띄어쓰기 없이 이어진 str을 split() 안 붙여도 됨
#     counting_number = {}
#     for i in arr:
#         counting_number[i] = 0
#     for i in arr:
#         counting_number[i] += 1
#
#     # 카드 개수 구하기
#     number_of_cards = 1
#     for i in counting_number:
#         if counting_number[i] > number_of_cards:
#             number_of_cards = counting_number[i]
#
#     # 가장 많이 나온 숫자 구하기
#     keys = []
#     for key, value in counting_number.items():
#         if value == number_of_cards:
#             keys.append(key)
#
#     max_mode_number = keys[0]
#     for k in keys:
#         if k > max_mode_number:
#             max_mode_number = k
#
#     print(f"#{t+1} {max_mode_number} {number_of_cards}")
    

# 입력
# 3
# 5
# 49679
# 5
# 08271
# 10
# 7797946543