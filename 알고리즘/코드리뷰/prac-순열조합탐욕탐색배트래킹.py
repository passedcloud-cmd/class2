###############
## 순열 ##########
###############
# def permutation(selected, remaining):
#     # 기저 조건
#     if not remaining:
#         print(selected)
#         return
#     #재귀 단계
#     for i in range(len(remaining)):
#         pick = remaining[i]
#         next_remaining = remaining[:i] + remaining[i+1:]
#         permutation(selected+[pick], next_remaining)

# permutation([], [1,2,3])



# import itertools ############################
# data_list = ['a','b','c','d']
# result_list  = list(itertools.permutations(data_list, 2))
# print(result_list)
# print(list(map(''.join, result_list)))
# #혹은
# for perm_tuple in itertools.permutations('ABCD',2):
#     print(''.join(perm_tuple), end = ' ')

# print()
# # 숫자 예시
# for perm_tuple in itertools.permutations(range(3)):
#     print(''.join(map(str, perm_tuple)), end = ' ')



# ###############
# ## 중복 순열 ##########
# ###############
# def rep_permutation(selected, arr, r):
#     # 기저 조건. 중복 순열은 remaining이 영원히 비지 않아서 뽑은 개수로 기저 조건을 걸어야 함
#     if len(selected) == r:
#         print(selected)
#         return
#     #재귀 단계
#     for i in range(len(arr)):
#         pick = arr[i]
#         rep_permutation(selected+[pick], arr, r)

# rep_permutation([], [1,2,3], 3)

# # 중복 순열
# import itertools #############################
# result = list(itertools.product('ABC', repeat=2))
# print(f'중복순열: {result}')





# ###############
# ## 조합 ##########
# ###############
# def combination(arr, r):
#     """
#     arr: 원본 배열
#     r: 뽑을 개수
#     """
#     # 기저 조건
#     if r == 0:
#         return [[]]

#     result = []
#     # 재귀 단계
#     for i in range(len(arr)):
#         # i번째 원소를 첫 번째 요소로
#         elem = arr[i]
#         next_arr = arr[i+1:]

#         for rest in combination(next_arr, r-1):
#             result.append([elem] + rest)

#     return result
# data = [1,2,3,4]
# combs = combination(data, 3)
# for c in combs:
#     print(c)


# import itertools ####################################
# data_list = ['A', 'B', 'C', 'D']
# result_list = list(itertools.combinations(data_list, 2))
# print(result_list)
# print(list(map(''.join, result_list)))
# # 혹은
# for comb_tuple in itertools.combinations('ABCD', 2):
#     print(''.join(comb_tuple), end=' ')

# print()
# # 숫자 예시
# for comb_tuple in itertools.combinations(range(4), 3):
#     print(''.join(map(str, comb_tuple)), end=' ')




# ###############
# ## 중복 조합 ##########
# ###############
# def combination(arr, r):
#     """
#     arr: 원본 배열
#     r: 뽑을 개수
#     """
#     # 기저 조건
#     if r == 0:
#         return [[]]

#     result = []
#     # 재귀 단계
#     for i in range(len(arr)):
#         # i번째 원소를 첫 번째 요소로
#         elem = arr[i]
#         next_arr = arr[i:] # 조합에선 arr[i+1:]이었음

#         for rest in combination(next_arr, r-1):
#             result.append([elem] + rest)

#     return result
# data = [1,2,3,4]
# combs = combination(data, 3)
# for c in combs:
#     print(c)


# import itertools #itertools 사용######################
# result = list(itertools.combinations_with_replacement('ABC', 2))
# print(f'중복순열: {result}')





# ###############
# ## 탐욕 알고리즘 ##########
# ###############
# def get_minimum_coins(coin_list, amount):
#     """
#     coin_list: 동전 금액 리스트 (예: [500, 100, 50, 10])
#     amount: 거슬러줄 총 금액 (예: 800)
#     return: {동전금액: 개수} 형태의 딕셔너리
#     """
#     result = {}
#     coin_list.sort(reverse=True)

#     for coin in coin_list:
#         if amount >= coin:
#             coin_count = amount // coin
#             amount -= coin_count * coin
#             result[coin] = coin_count

#     return result

# coins = [10, 50, 100, 500]
# change_amount = 800
# change_result = get_minimum_coins(coins, change_amount)
# for c, cnt in change_result.items():
#     print(f'{c}원 동전: {cnt}개')




#####################################
### 분할정복 - 병합 정렬, 퀵 정렬, 이진 서치
##################################

##############
### 병합 정렬 ##
### 시간 복잡도: O(NlogN)
##############
def merge(left_arr, right_arr):
    """
    이미 정렬된 두 배열(left_arr, right_arr)을
    하나의 정렬된 배열로 '병합'하는 함수
    """
    merged_arr = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1

    #extend() 함수는 리스트 끝에 반복 가능한 객체(iterable)의 모든 항목을 풀어서 각각 개별 원소로 추가할 때 사용
    merged_arr.extend(right_arr[right_idx:])
    merged_arr.extend(left_arr[left_idx:])

    return merged_arr

def merge_sort(arr):
    """
    병합 정렬을 재귀적으로 구현하는 '매니저' 함수
    """
    # 0. 기저 조건 
    if len(arr)<=1:
        return arr
    # 1. 절반 분할
    mid = len(arr) //2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. 재귀적으로 정렬
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 3. 통합
    return merge(left_sorted, right_sorted)

data = [69, 10, 30, 2, 16, 8, 31, 22]
print(f'merge sort 정렬 후: {merge_sort(data)}')


##############
### 퀵 정렬 ##
### 시간 복잡도: 평균 O(NlogN)​, 최악: O(N2)​
##############
import sys
sys.setrecursionlimit(10**6)

def partition(arr, start, end):
    """
    분할(Partition)을 담당하는 실무자 함수.
    - 가장 오른쪽 원소(arr[end])를 피벗으로 설정.
    - 피벗보다 작은 값들은 왼쪽으로, 큰 값들은 오른쪽으로 재배치.
    - 최종적으로 피벗이 있어야 할 올바른 위치의 인덱스를 반환.
    """
    pivot = arr[end]
    i = start -1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end] = arr[end], arr[i+1]

    return i+1

def quick_sort(arr, start, end):
    """
    퀵 정렬을 재귀적으로 지시하는 '매니저' 함수.
    """
    # 기저 조건: start>=end 면 배열 길이가 1이하여서 분할이 불가능. 끝. 
    if start < end:
        pivot_idx = partition(arr, start, end)

        quick_sort(arr, start, pivot_idx -1)
        quick_sort(arr, pivot_idx +1, end)

data = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(data, 0, len(data) - 1)
print(f"quick sort 정렬 후: {data}") 




##############
### 이진 서치 ##
### 시간 복잡도: O(logn)
##############
# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left<=right:
#         mid = (left + right) //2
#         if arr[mid] == target:
#             return mid
#         elif target < arr[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1

# numbers = [2, 4, 7, 9, 11, 19, 23]
# target_value = 11
# result = binary_search(numbers, target_value)
# print(f'목표값 인덱스: {result}')


def binary_search_recursive(arr, left, right, target):
    '''
    - arr  : 정렬된 리스트 (오름차순)
    - left : 현재 검색 범위의 시작 인덱스
    - right: 현재 검색 범위의 끝 인덱스
    - target: 찾고자 하는 값

    반환값:
    - target이 arr 안에 존재하면 해당 인덱스
    - 존재하지 않으면 -1
    '''
    if left > right:
        return -1

    mid = (left+right)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, left, mid - 1, target)
    else:
        return binary_search_recursive(arr, mid + 1, right, target)

numbers = [2, 4, 7, 9, 11, 19, 23]
result = binary_search_recursive(numbers, 0, len(numbers) - 1, 9)
print(f"목표 인덱스: {result}") 




##############
### 백트래킹 ##
##############
## 순열
def find_permutations(nums):
    """
    순열 탐색을 시작하고 최종 결과를 반환하는 메인 함수.
    """
    result = []
    # 각 숫자의 사용 여부를 기록할 리스트 (used[i]가 True이면 i번째 숫자는 사용 중)
    used = [False] * len(nums)

    