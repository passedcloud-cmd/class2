# input.txt 미사용
arr = list(range(1, 11))

# solution 1 (재귀, 가지치기)
def find_subsets(k, current_subset):
    """
    k: 현재 고려할 원소의 인덱스
    current_subset: 현재까지 만들어진 부분집합 리스트
    """
    # 가지치기 - 부분 집합의 합이 10을 초과하면 더 이상 탐색X
    if sum(current_subset) > 10:
        return

    # 종료 조건 - 모든 원소를 다 고려했다면
    if k == N:
        # 부분집합의 합이 정확히 10인 경우에만 출력
        if sum(current_subset) == 10:
            print(*current_subset) # 리스트를 깔끔하게 출력    
        return

    # [재귀 호출]
    # 1. k번째 원소를 부분집합에 포함하는 경우
    find_subsets(k+1, current_subset + [arr[k]])
    # 2. k번째 원소를 부분집합에 포함하지 않는 경우 
    find_subsets(k+1, current_subset)

arr = list(range(1, 11))
N = len(arr)
# k = 0 (0번 인덱스부터 시작)
find_subsets(0, [])




#solution 2 (백트래킹 표준)

# input.txt 미사용
arr = list(range(1, 11))
# K: 현재까지 고려한 원소의 개수
# current_sum : 현재까지 만들어진 부분집합의 합
def backtracking(k, current_sum, included):
    # 가지치기 - 현재 합이 10을 넘으면 유망하지 않으므로 중단
    if current_sum >10:
        return

    # [종료 조건] 모든 원소를 다 고려했다면 
    if k == N:
        # 합이 10일 때만 해답 처리
        if current_sum == 10:
            for i in range(N):
                if included[i]:
                    print(arr[i], end=' ')

            print()
        return

    # [재귀호출]
    # 다음 원소(k)를 포함하는 경우와 포함하지 않는 경우, 두 가지 후보에 대해 탐색
    
    # 1. k번째 원소를 포함하는 경우로의 탐색
    included[k] = True