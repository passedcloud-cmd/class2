import sys
sys.stdin = open('4839-이진탐색.txt')


def binary_search(arr, left, right, target, cnt):
    # 함수를 1번 시작할 때마다 cnt + 1
    cnt += 1

    # 시작페이지 > 끝페이지면 target을 찾지 못했다는 뜻. -1 출력
    if left > right:
        return -1

    # 중간 페이지는 시작페이지와 끝페이지의 중간. 2로 나눈 몫
    center = (left + right) // 2

    # 중간페이지를 찾았다면 cnt 출력
    if arr[center] == target:
        return cnt

    # 타겟이 중간페이지보다 작다면, 타겟은 왼쪽에 있다
    elif target < arr[center] :
        return binary_search(arr, left, center, target, cnt)

    # 타겟이 중간페이지보다 크다면, 타겟은 오른쪽에 있다
    elif target > arr[center] :
        return binary_search(arr, center, right, target, cnt)

T = int(input())
for test_case in range(1, T+1):
    # total은 전체 페이지 수(끝 페이지)
    # A_target과 B_target은 각각 찾아야할 페이지
    total, A_target, B_target = map(int, input().split())

    # range(0, total+1) = [0, 1, 2, 3, ... , total]
    # 위쪽 리스트에서 0은 더미 데이터. 책은 1페이지부터 시작하니까, 페이지 수와 인덱스를 일치시켰음.
    # 1페이지에서 시작, total페이지가 끝
    # cnt도 0에서 시작
    A_cnt = binary_search(range(0, total+1), 1, total, A_target, 0)
    B_cnt = binary_search(range(0, total+1), 1, total, B_target, 0)

    # 확인용 출력
    # print(f'A: {A_cnt}, B: {B_cnt}') 

    # cnt 수가 적은 사람이 승자
    if A_cnt < B_cnt:
        winner = 'A'
    elif A_cnt > B_cnt:
        winner = 'B'
    # A와 B의 cnt 수가 같다면 무승부. 0 출력
    else:
        winner = 0

    print(f'#{test_case} {winner}')