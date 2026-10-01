# 3단계: 이진 검색
#
# 학습 목표
#   - 탐색 범위를 반씩 줄여 가는 과정을 반복문과 재귀 두 가지로 쓸 수 있다.
#   - 확인한 mid 를 범위에서 빼야 하는 이유를 설명할 수 있다.
#
# 노션 '이진 검색' 2장과 같은 코드입니다.

numbers = [2, 4, 7, 9, 11, 19, 23]  # 이진 검색은 반드시 정렬된 리스트에서만 동작합니다


# ------------------------------------------------------------
# [실습 1] 반복문 방식
# ------------------------------------------------------------
def binary_search(arr, target):
    """target 의 인덱스를 돌려줍니다. 없으면 -1."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            # 1-1. 찾았습니다. mid 를 돌려주세요.
            return mid  # TODO
        elif target < arr[mid]:
            # 1-2. target 은 왼쪽 절반에 있습니다. right 를 옮기세요.
            #      mid 는 방금 확인했으니 범위에서 뺍니다.
            right = mid - 1 # TODO
        else:
            # 1-3. target 은 오른쪽 절반에 있습니다. left 를 옮기세요.
            left = mid + 1 # TODO

    return -1 # 값을 못 찬은 경우


print('반복문  19 ->', binary_search(numbers, 19), end='')
print('   10 ->', binary_search(numbers, 10))
print('(정답: 5, -1)')
print()


# ------------------------------------------------------------
# [실습 2] 재귀 방식
# ------------------------------------------------------------
def binary_search_recursive(arr, left, right, target):
    """arr[left..right] 에서 target 의 인덱스를 돌려줍니다. 없으면 -1."""
    
    # 2-1. 기저 조건: 탐색 범위가 비었으면(left 가 right 보다 크면) -1 을 돌려줍니다.
    #      이 칸을 가장 먼저 채우세요. 없으면 없는 값을 찾을 때 재귀가 끝나지 않습니다.
    if left > right:  # TODO
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        # 2-2. 왼쪽 절반으로 자기 자신을 부르고, 그 결과를 그대로 돌려주세요.
        #      return 을 빠뜨리면 안에서 찾은 답이 밖으로 나오지 못하고 None 이 됩니다.
        return binary_search_recursive(arr, left, mid - 1, target)  # TODO
    else:
        # 2-3. 오른쪽 절반으로 자기 자신을 부르고, 그 결과를 돌려주세요.
        return binary_search_recursive(arr, mid +1, right, target)  # TODO


last = len(numbers) - 1
print('재귀    11 ->', binary_search_recursive(numbers, 0, last, 11), end='')
print('   1 ->', binary_search_recursive(numbers, 0, last, 1))
print('(정답: 4, -1)')
