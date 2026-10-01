# 2단계: 퀵 정렬 (Lomuto 파티션)
#
# 학습 목표
#   - 피벗보다 작은 값을 왼쪽으로 모으는 파티션을 직접 짤 수 있다.
#   - 파티션이 끝나면 피벗이 제자리에 온다는 것을 확인한다.
#
# 노션 '퀵 정렬' 4장 코드에서 if i != j 분기만 뺀 형태입니다.


# ------------------------------------------------------------
# [실습 1] 파티션
# ------------------------------------------------------------
def partition(arr, start, end):
    """arr[end] 를 피벗으로 삼아 나누고, 피벗이 자리 잡은 인덱스를 돌려줍니다."""
    pivot = arr[end]
    i = start - 1  # start 부터 i 까지가 '피벗보다 작은 값' 구역. 처음엔 비어 있음. # i가 주황색. 경계선

    for j in range(start, end):
        # 1-1. arr[j] 가 피벗보다 작으면, i 를 1 늘린 뒤 arr[i] 와 arr[j] 를 바꾸세요.
        #      작은 값을 찾을 때마다 작은 값 구역을 한 칸 넓히고 그 자리로 데려오는 것입니다.
        # TODO
        if arr[j] < pivot:
            i += 1 # 경계선 하나 올림
            arr[i], arr[j] = arr[j], arr[i] # i와 j의 값이 같으면 변화 없음. 굳이 if문으로 나누지 않아도 됨.

    # for문이 끝나면 경계선 다음 칸과 피벗 바꾸지

    # 1-2. 작은 값 구역 바로 다음 칸(i + 1)과 피벗(arr[end])을 바꾸세요.
    #      이 한 줄로 피벗이 제자리에 옵니다.
    # TODO
    arr[i+1], arr[end] = arr[end], arr[i+1]

    return i + 1 # 피벗의 최종 위치


data = [3, 2, 4, 6, 9, 1, 8, 7, 5]
arr = data[:]
p = partition(arr, 0, len(arr) - 1)
print('1회차 분할 :', arr[:p], arr[p], arr[p + 1 :])
print('(정답: [3, 2, 4, 1] 5 [6, 8, 7, 9])')
print()


# ------------------------------------------------------------
# [실습 2] 재귀로 양쪽 정렬하기
# ------------------------------------------------------------
def quick_sort(arr, start, end):
    """arr[start..end] 를 제자리에서 정렬합니다. 돌려주는 값은 없습니다."""
    if start < end: # 요소가 1개 남을 때까지 진행.
        pivot_idx = partition(arr, start, end)

        # 2-1. 피벗을 뺀 왼쪽 구간과 오른쪽 구간을 각각 quick_sort 로 정렬하세요. 두 줄입니다.
        #      피벗은 이미 제자리이므로 범위에서 뺍니다.
        #      피벗을 범위에 넣으면 범위가 줄지 않아 RecursionError 가 납니다.
        # TODO
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)


quick_sort(data, 0, len(data) - 1)
print('정렬 후 :', data)
print('(정답: [1, 2, 3, 4, 5, 6, 7, 8, 9])')
