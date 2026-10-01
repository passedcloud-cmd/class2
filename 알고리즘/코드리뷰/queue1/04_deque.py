# ------------------------------------------------------------
# 04. Deque (Double-Ended Queue)
# ------------------------------------------------------------
# [비유] 양쪽이 뚫린 컨베이어 벨트
#   앞쪽 끝과 뒤쪽 끝 '모두'에서 넣고 뺄 수 있다.
#   그래서 deque 하나로 큐도 되고 스택도 된다.
#
# [왜 쓰나] list 는 맨 앞에서 넣고 빼면 뒤 요소를 전부 밀어야 해서 O(N) 이다.
#   deque 는 양 끝의 위치 정보(포인터)만 옮기므로 O(1) 이다.
#   02번에서 본 list.pop(0) 의 비효율, 03번에서 직접 만든 원형 큐 —
#   "앞에서 빼도 느려지지 않게" 라는 같은 문제를 파이썬이 C로 해결해 둔 것이
#   collections.deque 다. 단, 구현 방식은 원형 큐가 아니라 이중 연결 리스트다.
#
# [주요 연산]  모두 O(1)
#   append(x)      오른쪽 끝에 x 추가
#   appendleft(x)  왼쪽 끝에 x 추가
#   pop()          오른쪽 끝 요소 제거 후 반환
#   popleft()      왼쪽 끝 요소 제거 후 반환
#
# 시간복잡도: 양 끝 삽입/삭제 O(1) / 공간복잡도: O(N)
# ------------------------------------------------------------

import time
from collections import deque

# ------------------------------------------------------------
# 1. 기본 연산
# ------------------------------------------------------------
print('=== 1. deque 기본 연산 ===')

dq = deque([10, 20, 30])
print(f'  초기 상태        : {dq}')

dq.append(40)  # 오른쪽 끝에 추가
print(f'  append(40)      : {dq}')

dq.appendleft(0)  # 왼쪽 끝에 추가
print(f'  appendleft(0)   : {dq}')

right_item = dq.pop()  # 오른쪽 끝 제거
print(f'  pop() -> {right_item:<6} : {dq}')

left_item = dq.popleft()  # 왼쪽 끝 제거
print(f'  popleft() -> {left_item:<2} : {dq}')

# [주의] deque 는 인덱스 접근(dq[2])은 되지만 O(N) 이다.
#        가운데 삽입/삭제도 O(N). deque 의 장점은 어디까지나 '양 끝'이다.


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# 2. deque 하나로 큐도 되고 스택도 된다
# ------------------------------------------------------------
print('=== 2. 같은 자료구조, 다른 사용법 ===')

# 큐(FIFO): 오른쪽으로 넣고 왼쪽에서 꺼낸다
queue = deque()
for value in ['A', 'B', 'C']:
    queue.append(value)
print(f'  큐    : append 로 A,B,C 넣고 popleft -> ', end='')
print(', '.join(queue.popleft() for _ in range(3)), '(먼저 넣은 것이 먼저)')

# 스택(LIFO): 오른쪽으로 넣고 오른쪽에서 꺼낸다
stack = deque()
for value in ['A', 'B', 'C']:
    stack.append(value)
print(f'  스택  : append 로 A,B,C 넣고 pop     -> ', end='')
print(', '.join(stack.pop() for _ in range(3)), '(나중에 넣은 것이 먼저)')

print('  => 넣는 쪽은 같고, 꺼내는 쪽만 다르다. 그것이 FIFO 와 LIFO 의 차이다.')


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# 3. rotate() - 통째로 회전시키기
# ------------------------------------------------------------
# rotate(n)
#   n 이 양수 : 오른쪽으로 n 칸 회전 (오른쪽 끝 n개가 왼쪽으로 이동)
#   n 이 음수 : 왼쪽으로 n 칸 회전   (왼쪽 끝 n개가 오른쪽으로 이동)
print('=== 3. rotate() ===')

dq = deque([1, 2, 3, 4, 5])
print(f'  원본        : {list(dq)}')

dq.rotate(2)
print(f'  rotate(2)   : {list(dq)}   <- 오른쪽으로 2칸 (뒤의 4,5 가 앞으로)')

dq.rotate(-1)
print(f'  rotate(-1)  : {list(dq)}   <- 왼쪽으로 1칸')


# rotate 없이 같은 일을 하려면?
print('\n  [비교] rotate 없이 직접 구현하면')
manual = deque([1, 2, 3, 4, 5])
for _ in range(2):
    manual.appendleft(manual.pop())  # 오른쪽 끝을 떼어 왼쪽에 붙이기 = rotate(1)
print(f'    pop + appendleft 를 2번 : {list(manual)}')
print('    => 결과는 같지만 rotate(2) 한 줄이면 끝난다.')


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# [동작 과정 시각화] rotate 가 요소를 어떻게 옮기는지 보기
# ------------------------------------------------------------
def trace_rotate(values, steps):
    """rotate 를 한 칸씩 쪼개서 보여준다"""
    dq = deque(values)
    direction = '오른쪽' if steps > 0 else '왼쪽'
    print(f'  {list(dq)} 를 {direction}으로 {abs(steps)}칸 회전')
    print(f'    시작        : {list(dq)}')

    for step in range(abs(steps)):
        if steps > 0:
            moved = dq.pop()
            dq.appendleft(moved)
            action = f'끝의 {moved} 를 맨 앞으로'
        else:
            moved = dq.popleft()
            dq.append(moved)
            action = f'앞의 {moved} 를 맨 뒤로'
        print(f'    {step + 1}칸 이동    : {list(dq)}   ({action})')


print('=== rotate 과정 추적 ===')
trace_rotate([1, 2, 3, 4, 5], 2)
print()
trace_rotate([1, 2, 3, 4, 5], -2)


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# 4. maxlen - 크기를 고정하면 오래된 것이 밀려난다
# ------------------------------------------------------------
# deque 는 생성할 때 maxlen 을 주면 최대 길이가 고정된다.
# 꽉 찬 상태에서 한쪽에 넣으면, 반대쪽 끝이 자동으로 밀려 나간다.
print('=== 4. maxlen 으로 최근 N개만 유지하기 ===')

recent = deque(maxlen=3)  # 최근 3개만 유지

for value in [1, 2, 3, 4, 5]:
    recent.append(value)
    print(f'  append({value}) -> {list(recent)}')

# [기대 출력] 마지막 줄이 [3, 4, 5]
#   maxlen 없이 만들면 [1, 2, 3, 4, 5] 가 되어 버린다.

print('\n  appendleft 도 마찬가지로 반대쪽이 밀려난다')
recent2 = deque([1, 2, 3], maxlen=3)
recent2.appendleft(0)
print(f'  deque([1, 2, 3], maxlen=3).appendleft(0) -> {list(recent2)}   <- 오른쪽 끝 3 이 밀려남')

# [연결] 03번에서 % 연산으로 직접 만든 원형 큐와 같은 성질이다.
#        "고정된 크기, 꽉 차면 가장 오래된 것부터 밀려남" —
#        그 동작을 파이썬은 maxlen=N 한 줄로 제공한다.

print('\n  [주의] 넘친 데이터는 에러 없이 조용히 사라진다')
box = deque(maxlen=2)
for value in ['A', 'B', 'C', 'D']:
    box.append(value)
print(f"  'A','B','C','D' 를 maxlen=2 deque 에 넣으면 -> {list(box)}   (A, B 는 흔적도 없다)")

# [어디에 쓰나]
#   - 최근 N개 유지 : 최근 검색어, 최근 로그, 최근 접속 기록
#   - 슬라이딩 윈도우 : 일정 구간을 유지하며 데이터를 순회할 때
#   - 버퍼 : 오래된 데이터는 버려도 되는 임시 저장 공간


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# 5. list vs deque - 직접 재보기
# ------------------------------------------------------------
# 이론상 O(N) vs O(1) 이라고 배웠다. 실제로 얼마나 차이가 날까?
print('=== 5. 맨 앞에서 빼기: list vs deque 실측 ===')
print(f'  {"데이터 개수":>10} | {"list.pop(0)":>14} | {"deque.popleft()":>16} | {"배율":>8}')
print(f'  {"-" * 10} | {"-" * 14} | {"-" * 16} | {"-" * 8}')

for n in [10_000, 50_000, 100_000]:
    data_list = list(range(n))
    start = time.perf_counter()
    while data_list:
        data_list.pop(0)
    list_time = time.perf_counter() - start

    data_deque = deque(range(n))
    start = time.perf_counter()
    while data_deque:
        data_deque.popleft()
    deque_time = time.perf_counter() - start

    ratio = list_time / deque_time if deque_time > 0 else 0
    print(f'  {n:>10,} | {list_time:>13.4f}s | {deque_time:>15.4f}s | {ratio:>7.1f}배')

# [포인트] 데이터가 10배가 되면 list 는 약 100배 느려진다. (O(N^2))
#          deque 는 거의 비례해서만 늘어난다. (O(N))
#          BFS 처럼 큐에 수만 개가 들락거리는 알고리즘에서는 이 차이가 곧 시간 초과다.


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# 6. [연결] 01번 마이쮸를 deque 로 바꿔보기
# ------------------------------------------------------------
# 01번에서 queue.pop(0) 을 썼다. deque 로 바꾸면 무엇이 달라질까?
def mychu_with_deque(total_candy):
    queue = deque([(1, 1)])  # list -> deque
    last_student = 0
    next_student = 2

    while total_candy > 0:
        student_id, want = queue.popleft()  # pop(0) -> popleft()

        give = min(want, total_candy)
        total_candy -= give
        last_student = student_id

        if total_candy == 0:
            break

        queue.append((student_id, want + 1))
        queue.append((next_student, 1))
        next_student += 1

    return last_student


print('=== 6. 마이쮸를 deque 로 ===')
print(f'  결과: {mychu_with_deque(20)}번 학생  (01번 list 버전과 동일)')
print('  바뀐 것은 딱 두 줄이다.')
print("    queue = [(1, 1)]      ->  queue = deque([(1, 1)])")
print('    queue.pop(0)          ->  queue.popleft()')
print('  => 로직은 그대로 두고 자료구조만 바꿔도 성능이 달라진다.')


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# [정리] 언제 무엇을 쓸까
# ------------------------------------------------------------
#   상황                              | 선택
#   --------------------------------- | ----------------------------------
#   맨 뒤에서만 넣고 뺀다 (스택)        | list 로 충분 (append / pop)
#   맨 앞에서 빼는 일이 있다 (큐, BFS)  | deque (append / popleft)
#   양쪽 끝을 다 쓴다                   | deque
#   가운데 삽입·삭제·정렬이 잦다        | list
#   인덱스로 자주 접근한다              | list (deque 의 인덱스 접근은 O(N))
#
# [실전] BFS 문제에서 deque 는 사실상 공식이다.
#   from collections import deque
#   queue = deque([start])
#   while queue:
#       node = queue.popleft()
#       ...
#
#
# [흔한 실수 & 디버깅 팁]
# 1) import 를 빼먹기
#      deque 는 내장 타입이 아니다. from collections import deque 가 필요하다.
#
# 2) popleft() 를 pop(0) 으로 쓰기
#      deque 에서 pop(0) 은 TypeError 다. (deque.pop() 은 인자를 받지 않는다)
#      습관적으로 pop(0) 을 쓰다 여기서 걸리는 경우가 많다.
#
# 3) 빈 deque 에서 pop / popleft
#      IndexError 가 난다. while queue: 로 감싸거나 len 을 먼저 확인할 것.
#
# 4) deque 를 리스트처럼 슬라이싱하기
#      dq[1:3] 은 TypeError 다. 슬라이싱이 필요하면 list(dq) 로 바꿔야 한다.
#
# 5) 가운데 연산이 많은데 deque 를 쓰기
#      deque 는 '양 끝' 전용 최적화다. 가운데 삽입·삭제는 list 와 다를 바 없다.
