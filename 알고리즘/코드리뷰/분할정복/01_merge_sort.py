# 1단계: 병합 정렬
#
# 학습 목표
#   - 정렬된 두 리스트를 앞에서부터 하나씩 비교하며 합칠 수 있다.
#   - '반으로 나누기 -> 각자 정렬 -> 합치기' 를 재귀로 옮길 수 있다.
#
# 노션 '병합 정렬' 3장과 같은 코드입니다.


# ------------------------------------------------------------
# [실습 1] 정렬된 두 리스트 합치기
# ------------------------------------------------------------
def merge(left_arr, right_arr):
    """이미 정렬된 두 리스트를 하나의 정렬된 리스트로 합쳐 돌려줍니다."""
    merged_arr = []
    left_idx, right_idx = 0, 0


    while left_idx < len(left_arr) and right_idx < len(right_arr):
        # 1-1. 왼쪽 값이 오른쪽 값보다 작거나 같으면, 왼쪽 값을 merged_arr 에 넣고 left_idx 를 1 늘리세요.
        #      아니면 오른쪽 값을 넣고 right_idx 를 1 늘리세요.
        #      비교는 < 가 아니라 <= 입니다. 같을 때 왼쪽을 먼저 넣어야 안정 정렬이 됩니다.
        pass  # TODO

    # 1-2. while 이 끝나면 한쪽에만 원소가 남습니다. 남은 것을 merged_arr 뒤에 이어 붙이세요.
    #      어느 쪽이 남을지 모르므로 양쪽 모두 붙입니다. 두 줄입니다. (extend 와 슬라이싱)
    pass  # TODO

    return merged_arr


print('merge 확인 :', merge([2, 10, 30], [8, 16]))
print('(정답: [2, 8, 10, 16, 30])')
print()


# ------------------------------------------------------------
# [실습 2] 나누고, 정렬하고, 합치기
# ------------------------------------------------------------
def merge_sort(arr):
    """arr 을 정렬한 새 리스트를 돌려줍니다. arr 자체는 바꾸지 않습니다."""
    if len(arr) <= 1:
        return arr

    # 2-1. 가운데 인덱스 mid 를 구하고, arr 을 앞쪽 절반과 뒤쪽 절반으로 나누세요. (분할)
    mid = 0  # TODO
    left_half = []  # TODO
    right_half = []  # TODO

    # 2-2. 두 절반을 각각 merge_sort 로 정렬하세요. 자기 자신을 부르는 재귀입니다. (정복)
    left_sorted = left_half  # TODO
    right_sorted = right_half  # TODO

    # 2-3. 정렬된 두 절반을 merge 로 합쳐서 돌려주세요. (통합)
    return []  # TODO


data = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_data = merge_sort(data)

print('정렬 후 :', sorted_data)
print('(정답: [2, 8, 10, 16, 22, 30, 31, 69])')
print('원본   :', data, '<- 병합 정렬은 원본을 바꾸지 않습니다')
