# 2단계: 간선 정보로 트리 만들기 (자식 배열 방식)
#
# 학습 목표
#   - 노드가 중간중간 비어 있는 일반 이진 트리는 왜 인덱스 규칙을 못 쓰는지 설명할 수 있다.
#   - 간선 목록을 읽어 left / right 리스트를 직접 채울 수 있다.
#   - 리스트 크기를 왜 V + 1 로 잡는지 설명할 수 있다.
#
# 시간 복잡도: O(V)  - 간선 V-1 개를 한 번씩 훑는다
# 공간 복잡도: O(V)  - left, right 리스트

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / '02_input.txt')

# 1. 트리 정보 입력 받기
V = int(input())  # 정점(Vertex) 개수: 13

# [실습 1] 간선 개수 구하기
#   트리는 루트를 제외한 모든 노드가 부모를 정확히 하나씩 가집니다.
#   그 '부모와의 연결' 이 곧 간선입니다. 그렇다면 간선은 몇 개일까요?
E = 0  # TODO

edge = list(map(int, input().split()))

# 2. 트리 저장소 준비
# 노드 번호가 1번부터 시작하므로 V + 1 크기로 잡는다. (0번 인덱스는 더미)
# 초기값 0 은 '자식이 없음' 을 의미한다.
left = [0] * (V + 1)
right = [0] * (V + 1)

# 3. 간선 정보를 읽어 트리 채우기
#
# 주의: 아래 로직은 "같은 부모의 간선 중 왼쪽 자식이 먼저 입력된다" 는 전제를 씁니다.
#       입력 순서가 뒤바뀌면 좌/우가 통째로 뒤집혀 중위 순회 결과가 달라집니다.
#       문제에서 `부모 왼쪽자식 오른쪽자식` 처럼 자리를 지정해 준다면 그 자리대로 넣어야 합니다.
for i in range(E):
    # [실습 2] edge 리스트에서 부모와 자식을 한 쌍씩 꺼내기
    #   edge = [1, 2, 1, 3, 2, 4, ...] 처럼 '부모 자식 부모 자식 ...' 으로 들어 있습니다.
    #   i번째 쌍은 edge 의 몇 번, 몇 번 칸일까요?
    parent = 0  # TODO
    child = 0  # TODO

    # [실습 3] 자식을 왼쪽에 넣을지 오른쪽에 넣을지 결정하기
    #   부모의 왼쪽이 아직 비어 있으면(0이면) 왼쪽에, 이미 찼으면 오른쪽에 넣습니다.
    if left[parent] == 0:
        pass  # TODO
    else:
        pass  # TODO

# 4. 결과 확인
print('=== 트리 생성 완료 ===')
print(f'왼쪽 자식 정보  : {left}')
print(f'오른쪽 자식 정보: {right}')
print()
print('해석 예시')
print(f'  1번의 자식 -> 왼쪽 {left[1]}, 오른쪽 {right[1]}')
print(f'  3번의 자식 -> 왼쪽 {left[3]}, 오른쪽 {right[3]}')
print(f'  8번의 자식 -> 왼쪽 {left[8]}, 오른쪽 {right[8]}  (둘 다 0 이면 리프 노드)')
print()

# --- 동작 과정 시각화 (완성되어 있습니다) ---
# 간선을 하나씩 처리할 때 left / right 가 어떻게 채워지는지 따라가 본다.
print('=== 간선 정보 처리 과정 ===')
trace_left = [0] * (V + 1)
trace_right = [0] * (V + 1)

for i in range(V - 1):
    parent = edge[i * 2]
    child = edge[i * 2 + 1]

    if trace_left[parent] == 0:
        trace_left[parent] = child
        position = '왼쪽'
    else:
        trace_right[parent] = child
        position = '오른쪽'

    print(
        f'{i + 1:2d}번째 간선 ({parent} -> {child}) | '
        f'{parent}번의 {position}이 비어 있음 -> {position}에 배치 | '
        f'left[{parent}]={trace_left[parent]}, right[{parent}]={trace_right[parent]}'
    )

print()
