# ------------------------------------------------------------
# 01. 선형 큐 (Linear Queue)
# ------------------------------------------------------------
# [비유] 놀이공원 대기줄
#   가장 먼저 줄을 선 사람이 가장 먼저 놀이기구를 탄다.
#   => 선입선출 (FIFO, First-In First-Out)
#   스택(프링글스 통)과 정반대다. 스택은 나중에 넣은 것이 먼저 나온다.
#
# [front 와 rear]  큐의 양 끝을 가리키는 두 개의 인덱스
#   front : 데이터가 '나가는 창구'      -> dequeue 가 일어나는 위치
#   rear  : 줄의 '마지막 대기자'        -> enqueue 가 일어나는 위치
#
# [학습 목표] 큐가 비었는지 / 꽉 찼는지는 이 둘의 '상대적 위치'로 판단한다.
#   초기 상태 : front == rear == -1
#   빈 상태   : front == rear
#   포화 상태 : rear == capacity - 1   <- 바로 이 조건이 선형 큐의 한계다
# ------------------------------------------------------------


import time


class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity  # 큐의 최대 크기
        self.items = [None] * capacity  # 저장 공간
        self.front = -1  # 머리 (삭제 위치)
        self.rear = -1  # 꼬리 (삽입 위치)

    def is_empty(self):
        # TODO 1) 큐가 비어 있는 조건을 작성하세요.
        #   힌트: front 와 rear 가 같은 곳을 가리키면 비어 있는 것이다.
        return self.front == self.rear

    def is_full(self):
        # TODO 2) 선형 큐에서 꽉 찼다고 판단하는 조건을 작성하세요.
        #   힌트: rear 가 배열의 마지막 인덱스에 닿았는지 확인한다.
        #         마지막 인덱스는 capacity 가 아니라 capacity - 1 이다.
        # 선형 큐의 한계 - 앞쪽이 비어 있어도 이 조건은 True가 됨.
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        if self.is_full():
            print('Queue is Full!')
            return

        # TODO 3) rear 를 한 칸 옮기고, 그 자리에 item 을 저장하세요.
        #   [순서 주의] 먼저 옮기고 나서 저장한다. 반대로 하면 한 칸씩 어긋난다.
        self.rear += 1
        self.items[self.rear] = item

        print(f'Enqueue({item}) -> {self.items} | front:{self.front}, rear:{self.rear}')

    def dequeue(self):
        if self.is_empty():
            print('Queue is Empty!')
            return None

        # TODO 4) front 를 한 칸 옮기고, 그 자리의 값을 item 에 담으세요.
        #   [주의] front 는 -1 에서 시작한다. 옮기기 전에 접근하면
        #          파이썬 음수 인덱스 때문에 '마지막 요소'가 조용히 잡힌다.
        self.front += 1
        item = self.items[self.front]


        # (선택) 꺼낸 자리를 None 으로 비워 두면 상태를 눈으로 보기 좋다
        # self.items[self.front] = None
        self.items[self.front] = None

        print(f'Dequeue() -> {item} | {self.items} | front:{self.front}, rear:{self.rear}')
        return item # 가져온 항목 반환

    def peek(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        return self.items[self.front + 1]  # front 다음 위치의 항목 반환

    def get_size(self):
        # TODO 5) 큐에 들어 있는 항목의 개수를 반환하세요.
        #   힌트: rear 와 front 의 거리다. +1 이 필요한지 직접 세어 보고 판단할 것.
        return self.rear - self.front


# --- 실행 테스트 ---
print('=== 선형 큐 테스트 (크기 4) ===')
q = LinearQueue(4)

# 1. 큐 꽉 채우기
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(f'\n큐의 현재 크기: {q.get_size()}')
print(f'큐의 맨 앞 데이터 확인(peek): {q.peek()}')
print(f'큐 내부 리스트 상태: {q.items}\n')

# 2. 데이터 2개 꺼내기 (앞쪽 2칸이 비게 됨)
q.dequeue()
q.dequeue()

print(f'\n큐의 현재 크기: {q.get_size()}')
print(f'큐의 맨 앞 데이터 확인(peek): {q.peek()}')
print(f'큐 내부 리스트 상태: {q.items}')

# 3. [문제 상황] 빈 공간이 있는데도 추가 불가 (False Full)
print('\n--- False Full 발생 확인 ---')
q.enqueue(50)


print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [동작 과정 시각화] front / rear 포인터가 어디를 가리키는지 보기
# ------------------------------------------------------------
def draw_queue(items, front, rear):
    """배열과 front / rear 포인터 위치를 그림으로 출력"""
    width = 6
    index_line = ''.join(f'{i:^{width}}' for i in range(len(items)))
    value_line = ''.join(f'{str(v):^{width}}' for v in items)

    marks = []
    for i in range(len(items)):
        tag = ''
        if i == front:
            tag += 'F'
        if i == rear:
            tag += 'R'
        marks.append(f'{tag:^{width}}')

    print(f'    index : {index_line}')
    print(f'    data  : {value_line}')
    print(f'    ptr   : {"".join(marks)}')

    note = []
    if front == -1:
        note.append('front=-1 (배열 밖: 아직 아무것도 꺼내지 않음)')
    if rear == -1:
        note.append('rear=-1 (배열 밖: 아직 아무것도 넣지 않음)')
    if note:
        print(f'            {" / ".join(note)}')


def trace_linear_queue():
    """선형 큐의 상태 변화를 단계별로 추적"""
    capacity = 4
    items = [None] * capacity
    front = -1
    rear = -1

    print('  [초기 상태]')
    draw_queue(items, front, rear)

    for value in [10, 20, 30, 40]:
        rear += 1
        items[rear] = value
        print(f'\n  enqueue({value})  -> rear 를 +1 하고 그 자리에 저장')
        draw_queue(items, front, rear)

    print(f'\n  이제 rear == capacity - 1 ({rear} == {capacity - 1}) 이므로 is_full() 은 True')

    for _ in range(2):
        front += 1
        removed = items[front]
        items[front] = None
        print(f'\n  dequeue() -> {removed}   front 를 +1 하고 그 자리를 비움')
        draw_queue(items, front, rear)

    print('\n  [문제] 0번, 1번 칸이 분명히 비어 있는데도')
    print(f'         rear({rear}) == capacity - 1({capacity - 1}) 이므로 is_full() 은 여전히 True')
    print('         => 이것이 "False Full" (가짜 포화 상태) 이다.')


print('=== 선형 큐 동작 과정 추적 ===')
trace_linear_queue()


print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [해결의 실마리]
# ------------------------------------------------------------
# False Full 을 해결하는 방법은 두 가지를 생각해 볼 수 있다.
#   1) dequeue 할 때마다 남은 데이터를 전부 앞으로 한 칸씩 당긴다
#      -> 동작은 하지만 매번 O(N) 이라 큐의 장점(O(1))이 사라진다.
#      -> 사실 이것이 파이썬 list.pop(0) 이 느린 이유와 정확히 같다.
#   2) 배열의 끝과 처음이 연결되어 있다고 '가정' 하고 앞쪽 빈칸을 재활용한다
#      -> 이것이 03번에서 배울 원형 큐(Circular Queue) 다.


print('=== list.pop(0) 이 느린 이유도 같은 문제다 ===')
demo = [10, 20, 30, 40]
print(f'  원본            : {demo}')
print('  pop(0) 실행 시   : 30, 40 을 한 칸씩 앞으로 당겨야 한다')
demo.pop(0)
print(f'  결과            : {demo}  <- 뒤 요소를 전부 이동시켰다 (O(N))')
print('  => 큐가 길수록 느려진다. 그래서 실전에서는 collections.deque 를 쓴다. (04번)')

print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [실측] front / rear 방식은 정말 pop(0) 문제를 해결하는가
# ------------------------------------------------------------
class _BenchQueue:
    """실측 전용 최소 구현 (출력이 없는 것만 다르다)"""

    def __init__(self, capacity):
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        self.rear += 1
        self.items[self.rear] = item

    def dequeue(self):
        self.front += 1
        return self.items[self.front]


print('=== enqueue N개 + dequeue N개 소요 시간 ===')
print(f'  {"N":>8} | {"list.pop(0)":>13} | {"front/rear":>13} | {"배율":>7}')
print(f'  {"-" * 8} | {"-" * 13} | {"-" * 13} | {"-" * 7}')

for n in [20_000, 50_000, 100_000]:
    data = []
    start = time.perf_counter()
    for i in range(n):
        data.append(i)
    for _ in range(n):
        data.pop(0)
    list_time = time.perf_counter() - start

    bench = _BenchQueue(n)
    start = time.perf_counter()
    for i in range(n):
        bench.enqueue(i)
    for _ in range(n):
        bench.dequeue()
    fr_time = time.perf_counter() - start

    print(f'  {n:>8,} | {list_time:>12.4f}s | {fr_time:>12.4f}s | {list_time / fr_time:>6.0f}배')

# [포인트] front / rear 방식은 데이터를 '옮기지' 않는다.
#          어디까지 꺼냈는지 '기록만' 하므로 N 이 커져도 거의 비례해서만 느려진다.
#          => 이 클래스 구현은 교과서용 연습이 아니라,
#             list.pop(0) 의 O(N) 문제에 대한 첫 번째 해답이다.
#
#          다만 이 방식에도 한계가 남아 있다. 바로 위에서 본 False Full 이다.
#          그 해결은 03번 원형 큐에서 이어진다.


print('\n' + '=' * 60 + '\n')


# ------------------------------------------------------------
# [스스로 점검하기]
# ------------------------------------------------------------
# Q1. front 를 -1 이 아니라 0 으로 초기화하면 무엇이 달라질까?
#     "아직 아무것도 꺼내지 않았다"를 0 으로 표현할 수 있을까?
#
# Q2. front 가 -1 인 상태에서 self.items[self.front] 를 실행하면
#     에러가 날까, 아니면 어떤 값이 나올까? 직접 확인해 보자.
#
# Q3. enqueue 에서 저장을 먼저 하고 rear += 1 을 나중에 하면
#     배열이 어떻게 어긋날까?
#
# Q4. is_empty 를 len(self.items) == 0 으로 쓰면 왜 안 될까?
#     (힌트: items 는 처음부터 capacity 만큼 잡혀 있다)
#
# Q5. get_size 가 rear - front 인데 +1 이 필요 없는 이유는?
#     front 가 가리키는 자리는 '아직 안 꺼낸 데이터'일까, '이미 꺼낸 자리'일까?
