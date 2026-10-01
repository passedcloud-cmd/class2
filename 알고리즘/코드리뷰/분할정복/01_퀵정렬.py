import sys
sys.stdin = open("01_퀵정렬.txt")

# 피벗의 인덱스 위치를 찾는 함수
def find_pivot_position(arr, start, end):
    # 피벗값은 가장 뒤에 있는 값 
    pivot = arr[end]
    # 처음 경계선은 바깥에 있음
    i = start - 1

    # 첫 번째 값부터 피벗값 앞까지 반복
    for j in range(start, end):
        # arr[j]가 피벗값보다 크면 그냥 continue
        if arr[j] > pivot:
            continue
        # arr[j]가 피벗값보다 작거나 같으면 i를 +1 한 다음 arr[j]와 arr[i] 위치 바꾸기
        if arr[j] <= pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]

    # 피벗값 앞까지 for문을 다 돌았다면 i+1번째 값과 피벗값 위치 바꾸기
    arr[i+1], arr[end] = arr[end], arr[i+1]
    # i+1이 피벗의 최종 위치
    return i + 1

# 피벗을 기준으로 왼쪽과 오른쪽 덩어리를 정렬하는 함수
def quick_sort(arr, start, end):
    # start가 end보다 크거나 같으면 요소가 1개 남았다는 뜻
    # 요소가 1개면 이미 정렬이 된 셈이므로 요소가 1일 때가 기저 조건
    if start < end:
        # 피벗의 위치를 찾기
        pivot = find_pivot_position(arr, start, end)

        # 피벗 기준으로 왼쪽 덩어리
        quick_sort(arr, start, pivot-1)
        # 피벗 기준으로 오른쪽 덩어리
        quick_sort(arr, pivot+1, end)

# 입력값 T, arr 받아오기
T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))

    # 마지막 요소의 인덱스 번호 end는 len(arr)-1이라는 것을 주의! 
    quick_sort(arr, 0, len(arr)-1)

    # 함수가 실행되면서 원본 arr가 수정됨
    # " ".join() 함수로 리스트 내 값들 꺼내서 공백으로 이어주기
    print(f'#{test_case} {" ".join(map(str, arr))}')