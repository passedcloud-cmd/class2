"""
- heapq = 가장 급한 서류가 늘 맨 위에 올라와 있는 서류함. 서류함 전체가 정렬된 것은 아니다.
- 음수 트릭 = 점수를 거꾸로 적어 두기. 꼴찌부터 뽑는 기계로 1등부터 뽑는 방법.
"""

# heapq 모듈로 힙 쓰기

import heapq

numbers = [5, 3, 8, 4, 1, 2]

# [실습 1] 최소 힙
heap = numbers[:]
heapq.heapify(heap)  # 1-1
print('heapify 결과 :', heap)

small_first = []
while heap:  # 1-2
    small_first.append(heapq.heappop(heap))
print('작은 값부터  :', small_first)
print()

# [실습 2] 최대 힙 (음수 트릭)
max_heap = []
for num in numbers:  # 2-1
    heapq.heappush(max_heap, -num)

big_first = []
while max_heap:  # 2-2. 꺼낼 때 부호를 되돌리는 것을 잊지 않는다
    big_first.append(-heapq.heappop(max_heap))
print('큰 값부터    :', big_first)
print()

# [실습 3] 우선순위 큐 - 응급실 진료 순서
patients = [('김철수', 2), ('이영희', 5), ('박민수', 3), ('최지우', 5), ('정하늘', 1)]

waiting = []
for order, (name, level) in enumerate(patients):
    # 3-1. 위급도가 높을수록 먼저 -> 음수. 같으면 먼저 온 순 -> 도착 순번
    heapq.heappush(waiting, (-level, order, name))

call_order = []
while waiting:  # 3-2
    _, _, name = heapq.heappop(waiting)
    call_order.append(name)
print('진료 순서    :', call_order)
print()


# ============================================================
# 보조 자료 1 - heapify 하지 않은 리스트에서 꺼내면
# ============================================================
not_heap = numbers[:]
wrong = []
while not_heap:
    wrong.append(heapq.heappop(not_heap))
print('=== 보조 자료 1: heapify 없이 heappop ===')
print('결과:', wrong, ' <- 첫 값부터 5. heappop 은 리스트가 이미 힙이라고 믿는다')
print()


# ============================================================
# 보조 자료 2 - 순번이 없으면 누가 먼저 나올까
# ============================================================
print('=== 보조 자료 2: (우선순위, 이름) 만 넣었을 때 ===')
pair = [('최지우', 5), ('이영희', 5)]  # 최지우가 먼저 도착
no_order = []
for name, level in pair:
    heapq.heappush(no_order, (-level, name))
print(
    '먼저 나온 사람:', heapq.heappop(no_order)[1], ' <- 먼저 온 최지우가 아니라 글자 순'
)
