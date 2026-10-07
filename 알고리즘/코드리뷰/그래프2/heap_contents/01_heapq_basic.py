# heapq 모듈로 힙 쓰기
#
# 학습 목표
#   - heapify, heappush, heappop 으로 최소 힙을 쓸 수 있다.
#   - 음수 트릭으로 최대 힙을 만들 수 있다.
#   - (우선순위, 순번, 데이터) 튜플로 우선순위 큐를 만들 수 있다.
#
# 노션 'Heap (with heapq 모듈)' 2장, 4장과 같은 내용입니다.

import heapq

numbers = [5, 3, 8, 4, 1, 2]


# ------------------------------------------------------------
# [실습 1] 최소 힙
# ------------------------------------------------------------
heap = numbers[:]  # 원본을 지키려고 복사해서 씁니다

# 1-1. heap 리스트를 그 자리에서 최소 힙으로 바꾸세요.
heapq.heapify(heap)  # TODO

print('heapify 결과 :', heap) # [1, 3, 2, 4, 5, 8] 정렬한 거 아님. 맨 앞이 최소값.
print('(정답: [1, 3, 2, 4, 5, 8])')

# 1-2. 힙이 빌 때까지 하나씩 꺼내 small_first 에 차례로 담으세요.
#      heap[0] 으로 읽기만 하면 힙이 줄지 않아 반복이 끝나지 않습니다. heappop 으로 꺼내세요.
#      1-1 을 비워 둔 채로 이것부터 채워 보면, 결과가 어떻게 틀리는지 볼 수 있습니다.
small_first = []
while heap: # TODO
    pop_result = heapq.heappop(heap) #heapq.heapify(heap)를 하지 않고 heappop을 하면 이상하게 작동함
    small_first.append(pop_result)

print('작은 값부터  :', small_first)
print('(정답: [1, 2, 3, 4, 5, 8])')
print()


# ------------------------------------------------------------
# [실습 2] 최대 힙 (음수 트릭)
# ------------------------------------------------------------
max_heap = []

# 2-1. numbers 의 값마다 부호를 바꿔서 max_heap 에 넣으세요.
for number in numbers: # TODO
    heapq.heappush(max_heap, -number)


# 2-2. max_heap 이 빌 때까지 꺼내면서, 부호를 되돌려 big_first 에 담으세요.
#      (1-2 와 마찬가지로 heappop 으로 꺼내야 반복이 끝납니다.)
big_first = []
while max_heap: # TODO
    pop_result = -heapq.heappop(max_heap)
    big_first.append(pop_result)

print('큰 값부터    :', big_first)
print('(정답: [8, 5, 4, 3, 2, 1])')
print()


# ------------------------------------------------------------
# [실습 3] 우선순위 큐 - 응급실 진료 순서
# ------------------------------------------------------------
# 위급도가 높은 환자부터 진료합니다. 위급도가 같으면 먼저 온 환자가 먼저입니다.
# (이름, 위급도) 가 도착한 순서대로 들어 있습니다.
patients = [('김철수', 2), ('이영희', 5), ('박민수', 3), ('최지우', 5), ('정하늘', 1)]

waiting = []

# 3-1. 환자마다 (우선순위, 도착 순번, 이름) 튜플을 waiting 에 넣으세요.
#      - heapq 는 작은 값부터 꺼냅니다. 위급도가 '높은' 환자가 먼저 나오려면? # 최대힙
#      - 도착 순번은 enumerate 로 얻을 수 있습니다. 위급도가 같을 때 순서를 정해 줍니다.
for order, (name, level) in enumerate(patients):
    heapq.heappush(waiting, (-level, order, name))  # TODO
    # 최대힙으로 만들기 위해 level에 마이너스를 붙임

# print(waiting)
# [(-5, 1, '이영희'), (-5, 3, '최지우'), (-3, 2, '박민수'), (-2, 0, '김철수'), (-1, 4, '정하늘')]


# 3-2. waiting 이 빌 때까지 꺼내서, 이름만 call_order 에 담으세요.
#      (heappop 으로 꺼내야 반복이 끝납니다.)
call_order = []
while waiting:  # TODO
    _, _, name = heapq.heappop(waiting)
    call_order.append(name)

print('진료 순서    :', call_order)
print("(정답: ['이영희', '최지우', '박민수', '김철수', '정하늘'])")
