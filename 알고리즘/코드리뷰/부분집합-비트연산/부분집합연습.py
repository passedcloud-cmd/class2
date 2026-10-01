#반복문 - 중첩 루프
selected = [0] * 3 # 원소가 3개일 시

for i in range(2): 
    selected[0] = i
    for j in range(2):
        selected[1] = j
        for m in range(2):
            selected[2] = m

            #부분집합 생성
            subset = []
            for n in range(3):
                if selected[n] == 1:
                    subset.append(n+1)

            print(f'반복문-중첩루프:{subset}')

# 재귀 방식
# depth번째 원소를 포함/미포함 두 갈래로 탐색
# 재귀 깊이가 전체 원소 수(len(input_list))에 도달하면, 현재까지 포함 상태를 토대로 부분집합 생성
# 재귀 호출 전후로 included[depth] 값을 수정(Backtracking)하며 모든 경우 탐색
def generated_subset(depth, included):
    """
    depth: 현재 확인할 원소 인덱스
    included: 각 원소가 포함됐는지(True/False)를 기록
    """
    # 모든 원소를 결정한 시점 - base line
    if depth == len(input_list):
        # included 상태에 따라 부분집합 생성
        current_subset = [input_list[i] for i in range(len(input_list)) if included[i]]
        subsets.append(current_subset)
        return

    # (1) 현재 원소를 포함하지 않는 경우
    included[depth] = False
    generated_subset(depth + 1, included)

    # (2) 현재 원소를 포함하는 경우
    included[depth] = True
    generated_subset(depth + 1, included)

input_list = [1,2,3]
subsets = []
init_included = [False] * len(input_list)

generated_subset(0, init_included)

print(f'재귀방식:{subsets}')

#비트 연산
# AND a&b : 두 비트가 1인 경우만 1
# OR a|b : 두 비트 중 하나만 1이어도 1
# XOR a^b : 두 비트 중 하나만 1이어야 1
# NOT ~A : 비트를 반대로 뒤집어서 반환
# 시프트 a<<1 : 비트를 왼쪽으로 1칸 이동. 즉 2배
# 시프트 a<<3 : 비트를 왼쪽으로 3칸 이동. 즉 2^3 = 8배
# 시프트 a>>2 : 비트를 오른쪽으로 2칸 이동. 즉 1/4배
print(0b1111) # 15
print(0b1111<<1) # 30
print(0b1111<<2) # 60
print(0b1111>>2) # 3

# 비트를 부분 집합에서 활용
nums = [3, 6, 7, 1]
n = len(nums)
cnt = 0
#모든 부분집합의 개수만큼 반복하자
for i in range(1<<n): #64번 체크
    # 부분집합 개수 체크
    cnt += 1
    # 모든 원소 개수만큼 반복
    for j in range(n):
        # i의 값과 (1 << j)의 결과로 나오는 j값(인덱스)
        if i & (1<<j):
            print(nums[j], end=',')
print(cnt) 

# 예쁘게 정리
nums = [3, 6, 7, 8]
n = len(nums)
subset_cnt = 2**n # 8
subsets = []
for i in range(subset_cnt):
    subset = []
    for j in range(n):
        # i의 j번째 비트가 1인지 확인
        if i & (1 << j):
            subset.append(nums[j])
    subsets.append(subset)
print(subsets)

# 응용 예시 - “합이 10인 부분집합” 출력**
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
subset_cnt = 2**n

for i in range(subset_cnt):
    subset = []
    total = 0
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])
            total += arr[j]
    if total == 10:
        print(f'합이 10인 부분집합: {subset}')