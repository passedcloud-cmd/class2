# 0단계: 병합 정렬 백지에서 끝까지 써 보기
#
# 주석 바로 아래에 직접 써 넣으세요.
#
# 순서
#   [1] 입력            N, 숫자 리스트 읽기
#   [2] merge 함수      정렬된 두 리스트를 하나로 합치기
#   [3] merge_sort 함수 반으로 나누고, 각각 정렬하고, 합치기
#   [4] 실행과 출력
#
# 이 이름들을 그대로 쓰세요 (맨 아래 정답 확인이 이 이름을 찾습니다)
#   N   numbers   merge   merge_sort   sorted_numbers
#
# 00_input.txt
#   8                            <- 숫자 개수
#   69 10 30 2 16 8 31 22        <- 정렬할 숫자들

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  
sys.stdin = open(BASE_DIR / '00_input.txt')  


# ============================================================
# [1] 입력
# ============================================================
# 1-1. 첫 줄을 읽어 N 에 정수로 담으세요.
N = int(input())
# 1-2. 둘째 줄을 읽어 정수 리스트로 만들어 numbers 에 담으세요.
numbers = list(map(int, input().split()))

# ============================================================
# [2] merge 함수 - 이미 정렬된 두 리스트를 하나로 합치기
# ============================================================
# 2-1. merge 라는 함수를 정의하세요. 매개변수는 left_arr, right_arr 두 개입니다.
#      (2-2 부터 2-10 까지는 전부 이 함수 안입니다. 들여쓰기에 주의하세요)
def merge(left_arr, right_arr):

    # 2-2. 합친 결과를 담을 빈 리스트 merged 를 만드세요.
    merged = []


    # 2-3. 두 리스트에서 지금 보고 있는 위치 left_idx, right_idx 를 0 으로 만드세요.
    #      한 줄에 두 변수를 함께 만들 수 있습니다.
    left_idx = 0
    right_idx = 0

    # 2-4. 두 리스트 '모두' 에 아직 볼 원소가 남아 있는 동안 반복하는 while 문을 여세요.
    #      둘 중 하나라도 바닥나면 멈춰야 합니다. and 일까요, or 일까요?
    #      (2-5 부터 2-8 까지는 이 while 안입니다)
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        # 2-5. 왼쪽의 현재 값이 오른쪽의 현재 값보다 작거나 같다면, 이라는 if 문을 여세요.
        #      '같다' 를 포함하는 이유: 값이 같으면 왼쪽 것을 먼저 넣어야 원래 순서가 유지됩니다.
        if left_arr[left_idx] <= right_arr[right_idx]:
            # 2-6. 왼쪽 값을 merged 에 넣고, left_idx 를 1 늘리세요. 두 줄입니다.
            merged.append(left_arr[left_idx])
            left_idx += 1
        # 2-7. 그렇지 않다면(else), 을 여세요.
        else:
            # 2-8. 오른쪽 값을 merged 에 넣고, right_idx 를 1 늘리세요. 두 줄입니다.
            merged.append(right_arr[right_idx])
            right_idx += 1

    # 2-9. while 이 끝나면 한쪽에만 원소가 남아 있습니다. 남은 것을 merged 뒤에 통째로 붙이세요.

    #      어느 쪽이 남았는지 몰라도 됩니다. 두 쪽 모두 붙이는 코드를 쓰면, 빈 쪽은 아무것도
    #      붙지 않습니다. 두 줄입니다. (while 밖, 함수 안)
    merged.extend(left_arr[left_idx:]) # 슬라이싱의 결과는 리스트이기 때문에 append하지 않기
    # extend는 반복 가능한 객체를 풀어서 리스트에서 추가
    merged.extend(right_arr[right_idx:])

    # 2-10. merged 를 돌려주세요.
    return merged

# 2-11. merge 가 잘 되는지 확인해 보세요. 함수 밖입니다. 확인했으면 지워도 됩니다.
#       merge([2, 10, 30], [8, 16]) 을 출력하면 [2, 8, 10, 16, 30] 이 나와야 합니다.
print('merge 확인:', merge([2, 10, 30], [8, 16]))


# ============================================================
# [3] merge_sort 함수 - 나누고, 각각 정렬하고, 합치기
# ============================================================
# 3-1. merge_sort 라는 함수를 정의하세요. 매개변수는 arr 하나입니다.
#      (3-2 부터 3-6 까지는 전부 이 함수 안입니다)
def merge_sort(arr):
    # 3-2. 기저 조건: arr 의 길이가 1 이하라면 arr 을 그대로 돌려주세요. 두 줄입니다.
    #      원소가 하나뿐인 리스트는 이미 정렬된 상태입니다. 여기가 재귀가 멈추는 곳입니다.
    if len(arr) <= 1:
        return arr
    
    # 3-3. 가운데 인덱스를 mid 에 담으세요. 길이를 2 로 나눈 몫입니다.
    mid = len(arr) // 2

    # 3-4. arr 을 앞쪽 절반 left_half 와 뒤쪽 절반 right_half 로 나누세요. 두 줄입니다.
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 3-5. 두 절반을 각각 merge_sort 로 정렬해서 left_sorted, right_sorted 에 담으세요. 두 줄입니다.
    #      자기 자신을 부르는 재귀입니다. "반쪽은 정렬되어 돌아온다" 고 믿고 쓰세요.
    sorted_left_arr = merge_sort(left_half)
    sorted_right_arr = merge_sort(right_half)

    # 3-6. 정렬된 두 절반을 merge 로 합쳐서 돌려주세요.
    return merge(sorted_left_arr, sorted_right_arr)


# ============================================================
# [4] 실행과 출력
# ============================================================
# 4-1. numbers 를 merge_sort 로 정렬해서 sorted_numbers 에 담으세요.
sorted_numbers = merge_sort(numbers)
# 4-2. sorted_numbers 의 숫자를 공백 한 칸씩 띄워서 한 줄로 출력하세요.
print(*sorted_numbers)


# --- 정답 확인 (고치지 마세요) ---
if 'sorted_numbers' in globals():
    answer = ' '.join(map(str, sorted_numbers))
    expected = '2 8 10 16 22 30 31 69'
    print('통과' if answer == expected else f'틀렸습니다. 정답은 {expected}')
    if numbers != [69, 10, 30, 2, 16, 8, 31, 22]:
        print('주의: 원본 numbers 가 바뀌었습니다. 새 리스트를 돌려줘야 합니다.')
else:
    print('sorted_numbers 가 아직 없습니다. [4] 까지 완성하고 다시 실행하세요.')
