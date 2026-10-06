# import sys
# sys.stdin = open('input_practice.txt', encoding='utf-8')
# text = sys.stdin.read()
# print(text)

# import sys
# sys.stdin = open('input_practice.txt', encoding='utf-8')
# while True:
#     try:
#         line = input()
#         print(line)
#     except EOFError:
#         break

# ## trye except finally연습
# try:
#     num = int(input())
#     print(10/num)
# except ValueError as e:
#     print("숫자가 아니에요", e)
# except ZeroDivisionError as e:
#     print('0으로는 못 나눠', e)
# else:
#     print("계산성공")
# finally:
#     print("제대로 하자")






# # solution 1 (재귀, 가지치기)
# def find_subsets(k, current_subset):
#     """
#     k: 현재 고려할 원소의 인덱스
#     current_subset: 현재까지 만들어진 부분집합 리스트
#     """
#     # 가지치기 - 부분 집합의 합이 10을 초과하면 더 이상 탐색X
#     if sum(current_subset) > 10:
#         return

#     # 종료 조건 - 모든 원소를 다 고려했다면
#     if k == N:
#         # 부분집합의 합이 정확히 10인 경우에만 출력
#         if sum(current_subset) == 10:
#             print(current_subset) # 리스트를 깔끔하게 출력    
#         return

#     # [재귀 호출]
#     # 1. k번째 원소를 부분집합에 포함하는 경우
#     find_subsets(k+1, current_subset + [arr[k]])
#     # 2. k번째 원소를 부분집합에 포함하지 않는 경우 
#     find_subsets(k+1, current_subset)

# arr = list(range(1, 11))
# N = len(arr)
# # k = 0 (0번 인덱스부터 시작)
# print("==solution 1 (재귀, 가지치기)==")
# find_subsets(0, [])
# print()




# #solution 2 (백트래킹 표준)

# # K: 현재까지 고려한 원소의 개수
# # current_sum : 현재까지 만들어진 부분집합의 합
# # included: 각 원소의 포함 여부를 저장하는 배열
# def backtracking(k, current_sum, included):
#     # 가지치기 - 현재 합이 10을 넘으면 유망하지 않으므로 중단
#     if current_sum > 10:
#         return

#     # [종료 조건] 모든 원소를 다 고려했다면 
#     if k == N:
#         # 합이 10일 때만 해답 처리
#         if current_sum == 10:
#             for i in range(N):
#                 if included[i]:
#                     print(arr[i], end=' ')

#             print()
#         return

#     # [재귀호출]
#     # 다음 원소(k)를 포함하는 경우와 포함하지 않는 경우, 두 가지 후보에 대해 탐색
    
#     # 1. k번째 원소를 포함하는 경우로의 탐색
#     included[k] = True
#     backtracking(k+1, current_sum+arr[k], included)

#     # 2. k번째 원소를 포함하지 않는 경우로의 탐색(백트래킹)
#     included[k] = False
#     backtracking(k+1, current_sum, included)

# arr = list(range(1, 11))
# N = len(arr)
# included = [False] * N
# backtracking(0, 0, included)




# # 조합으로 풀기
# from itertools import combinations

# arr = list(range(1, 11))
# N = len(arr)
# target_sum = 10

# # 조건에 맞는 부분집합을 찾아 리스트에 저장
# valid_subsets = [] 
# for k in range(1, N+1):
#     # arr에서 k개의 원소로 만들 수 있는 모든 조합을 생성
#     for subset in combinations(arr, k):
#         # 해당 조합의 합이 10이면
#         if sum(subset) == target_sum:
#             valid_subsets.append(subset)

# valid_subsets.sort()#리스트 내부 튜플들을 정렬

# print(valid_subsets)
# for subset in valid_subsets:
#     print(subset)



# # 플래그 배열(bit)
# def find_subsets_with_bit(k):
#     """
#     k: 현재 포함 여부를 결정할 원소의 인덱스
#     """
#     # 종료조건 - 모든 원소의 포함 여부를 결정했다면
#     if k == N:
#         subset_sum = 0
#         current_subset = []
#         # bit 배열을 보고 1로 표시된 원소만 골라 합과 부분집합을 만듦
#         for i in range(N):
#             if bit[i] == 1:
#                 subset_sum += arr[i]
#                 current_subset.append(arr[i])

#         # 합이 10이면 출력
#         if subset_sum == 10:
#             print(current_subset)
#         return

#     # 재귀 호출
#     # 1. k번째 원소를 포함하고 다음 원소로 이동
#     bit[k] = 1
#     find_subsets_with_bit(k+1)
#     # 2. k번째 원소를 포함하지 않는 경우를 탐색하기 위해 표시를 원래대로 되돌림
#     bit[k] = 0
#     find_subsets_with_bit(k+1)

# arr = list(range(1,11))
# N = len(arr)
# bit = [0] * N
# find_subsets_with_bit(0)



# #비트 마스크
# arr = list(range(1, 11))
# N = len(arr)
# for element in range(1<<N): # 1 x 2^N
#     sum_sub = 0
#     sub = []
#     for i in range(N): # arr 리스트의 모든 요소를 하나씩 검사
#         if element&1: # element(2진수)끝자리가 1이면 arr[i]의 스위치가 켜져 있단 뜻
#             sum_sub += arr[i]
#             # 합이 10 이상이면 중단하고 다음 부분집합으로 넘어가기
#             if sum_sub > 10: 
#                 break # for i
#             # 그렇지 않으면 sub 리스트에 arr[i] 추가
#             else: sub.append(arr[i])
#         # element(2진수)를 오른쪽으로 한칸 이동    
#         element >>= 1
#     # 합이 10인 부분집합들만 출력
#     if sum_sub == 10:
#         print(' '.join(map(str, sub)))