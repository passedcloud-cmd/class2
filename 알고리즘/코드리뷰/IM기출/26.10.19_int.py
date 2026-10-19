import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # N은 탑의 개수, K는 최대 작업 횟수
    N, K = map(int, input().split())
    # arr는 탑 리스트
    arr = list(map(int, input().split()))

    # 최소 불균형도는 최대치를 설정하고 시작
    min_height_diff = float('inf')

    # K가 0이 될때까지 진행
    while K > 0:
        # 만약 불균형도가 0이라면 반복문 종료
        if max(arr) == min(arr):
            min_height_diff = 0
            break # while

        # 가장 높은 탑 찾기
        for i in range(N):
            if arr[i] == max(arr):
                # 가장 높은 탑의 인덱스
                max_height = i

        # 가장 낮은 탑 찾기
        for j in range(N):
            if arr[j] == min(arr):
                # 가장 낮은 탑의 인덱스
                min_height = j

        # 가장 높은 탑에서 가장 낮은 탑으로 돌 옮기기
        arr[max_height] -= 1
        arr[min_height] += 1

        # 한 번 옮길 때마다 K 횟수도 1 차감
        K -= 1

        # 불균형도는 높은 탑과 낮은 탑의 차이
        height_diff = max(arr) - min(arr)
        # 최소 불균형도 경신
        min_height_diff = min(min_height_diff, height_diff)

    # 만약 K가 처음부터 0이어서 최소 불균형도가 경신된 적 없다면
    if min_height_diff == float('inf'):
        height_diff = max(arr) - min(arr)
        min_height_diff = min(min_height_diff, height_diff)

    print(f'#{test_case} {min_height_diff}')

#1 2
#2 0
#3 0

    # print("#%d" % test_case)
    # print("#%d" % test_case, min_height_diff)