# ------------------------------------------------------------
# 03. 원형 큐 (Circular Queue)
# ------------------------------------------------------------
# 02번에서 선형 큐의 "False Full" 문제를 확인했다.
# 앞쪽이 비어 있는데도 rear 가 끝에 닿았다는 이유로 더 못 넣는 문제였다.
#
# [해결 아이디어] 배열의 끝과 처음이 연결되어 있다고 '가정'한다.
#   시계에서 12시 다음이 1시이듯, 마지막 인덱스 다음은 다시 0번 인덱스.
#   이 순환을 코드로 만드는 도구가 바로 모듈러 연산(%) 이다.
#
#       (rear + 1) % capacity
#
#   capacity 가 5라면:  3 -> 4 -> 0 -> 1 -> 2 -> 3 ...
#
# [비유] 회전 초밥 레일
#   레일은 한정된 길이지만 계속 돌기 때문에 빈 자리를 몇 번이고 재활용한다.
#
# [학습 목표] 큐가 '비었을 때'와 '꽉 찼을 때' 모두 front == rear 가 되어 구분이 안 된다.
#   => 해결: 한 칸을 의도적으로 비워 둔다. (capacity 를 +1 해서 잡는다)
#      공백 : front == rear
#      포화 : (rear + 1) % capacity == front
# ------------------------------------------------------------


class CircularQueue:
    def __init__(self, capacity):
        # TODO 1) 공백/포화 상태를 구분하려면 실제 배열을 몇 칸으로 잡아야 할까?
        #   힌트: 한 칸을 의도적으로 비워 둔다. 3개를 담고 싶으면 배열은 4칸.
        self.capacity = capacity + 1

        self.items = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        # front와 rear 포인터가 같은 위치를 가리키면 큐는 비어있음
        return self.front == self.rear

    def is_full(self):
        # TODO 2) 원형 큐가 꽉 찼는지 판단하는 조건을 작성하세요.
        #   힌트: rear 의 '다음 칸'이 front 와 같으면 꽉 찬 것이다.
        #         다음 칸을 구할 때 모듈러 연산(%)을 써야 끝에서 0으로 돌아간다.
        #   [주의] 선형 큐의 rear == capacity - 1 을 그대로 쓰면 안 된다.
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print('Queue is Full!')
            return None

        # TODO 3) rear 포인터를 순환 이동시킨 뒤, 그 자리에 데이터를 저장하세요.
        #   힌트: (현재 rear + 1) % 전체 크기
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        print(
            f'Enqueue({item}) -> {self.items} | front:{self.front}, rear:{self.rear}'
        )

    def dequeue(self):
        if self.is_empty():
            print('Queue is Empty!')
            return None

        # TODO 4) front 포인터를 순환 이동시킨 뒤, 그 자리의 데이터를 가져오세요.
        self.front = (self.front + 1) % self.capacity
        item = self.items[self.front]

        # (선택) 삭제된 자리 비우기
        self.items[self.front] = None

        print(
            f'Dequeue() -> {item} | {self.items} | front:{self.front}, rear:{self.rear}'
        )
        return item

    def peek(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        # front의 '다음' 위치가 큐의 실제 시작점
        return self.items[(self.front + 1) % self.capacity]

    def get_size(self):
        # TODO 5) 현재 큐에 들어 있는 개수를 반환하세요.
        #   힌트: rear - front 로 구하면 순환한 경우 음수가 나온다.
        #         + capacity 를 더한 뒤 % capacity 를 하면 두 경우가 한 식으로 처리된다.
        return (self.rear - self.front + self.capacity) % self.capacity



# --- 실행 테스트 ---
print('=== 원형 큐 테스트 (크기 3) ===')
cq = CircularQueue(3)
print(f'내부 배열(실제 크기 {cq.capacity}): {cq.items}\n')

# 1. 가득 채우기
cq.enqueue('A')
cq.enqueue('B')
cq.enqueue('C')
cq.enqueue('D')  # Full (공간 하나 남겨두므로 3개 넣으면 꽉 참)

# 2. 하나 꺼내고 다시 채우기 (순환 확인)
print('\n--- 하나 꺼내고 다시 넣기 ---')
cq.dequeue()  # A 삭제 (앞쪽 공간 빔)
cq.enqueue('D')  # D 추가 (앞쪽 빈 공간 재활용!)
print(f'\n현재 크기: {cq.get_size()}, 맨 앞 데이터: {cq.peek()}')
print('=> 선형 큐였다면 여기서 "Queue is Full!" 이 떴을 것이다.')


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# [동작 과정 시각화] 포인터가 배열 끝에서 0으로 돌아가는 순간 보기
# ------------------------------------------------------------
def draw_circular(items, front, rear):
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


def trace_circular():
    """원형 큐의 순환 과정을 단계별로 추적 (실제 배열 크기 4 = 데이터 3칸)"""
    capacity = 4  # CircularQueue(3) 의 내부 크기
    items = [None] * capacity
    front = 0
    rear = 0

    print('  [초기 상태] front == rear == 0  =>  공백')
    draw_circular(items, front, rear)

    for value in ['A', 'B', 'C']:
        rear = (rear + 1) % capacity
        items[rear] = value
        print(
            f'\n  enqueue({value})   rear = (rear + 1) % {capacity} = {rear}'
        )
        draw_circular(items, front, rear)

    print(
        f'\n  (rear + 1) % {capacity} = {(rear + 1) % capacity} == front({front})  =>  포화'
    )
    print('  1칸(0번)을 일부러 비워 두었기 때문에 공백과 포화가 구분된다.')

    front = (front + 1) % capacity
    removed = items[front]
    items[front] = None
    print(f'\n  dequeue() -> {removed}   front = {front}')
    draw_circular(items, front, rear)

    rear = (rear + 1) % capacity
    items[rear] = 'D'
    print(
        f'\n  enqueue(D)   rear = (rear + 1) % {capacity} = {rear}  <- 끝에서 0으로 되돌아왔다!'
    )
    draw_circular(items, front, rear)
    print('  => 앞쪽 빈칸(0번)을 재활용했다. 이것이 원형 큐의 전부다.')


print('=== 원형 큐 동작 과정 추적 ===')
trace_circular()


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# [모듈러 연산 감 잡기] % 가 무슨 일을 하는지 숫자로 보기
# ------------------------------------------------------------
print('=== capacity 가 4일 때 (i + 1) % 4 의 값 ===')
print(f'  {"i":>3} | {"(i + 1) % 4":>12}')
print(f'  {"-" * 3} | {"-" * 12}')
for i in range(5):
    print(f'  {i:>3} | {(i + 1) % 4:>12}')
print('  => 3 다음이 0 이 된다. 배열의 끝과 처음이 연결되는 지점이다.')


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# [참고] 공간 낭비 없는 원형 큐 (count 변수 활용)
# ------------------------------------------------------------
# 1칸을 비워 두는 것이 아깝다면, 개수를 세는 변수(count)를 따로 두면 된다.
#   count == 0        : 비어있음
#   count == capacity : 꽉 참 (배열 끝까지 다 사용)
class CircularQueueFull:
    def __init__(self, capacity):
        self.capacity = capacity  # 최대 용량 (+1 하지 않는다)
        self.items = [None] * capacity
        self.front = 0  # 맨 앞 데이터를 가리킴
        self.rear = 0  # 다음 데이터가 들어갈 빈 자리를 가리킴
        self.count = 0  # [핵심] 현재 저장된 데이터 개수

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print('Queue is Full!')
            return

        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity  # rear 순환 이동

        # TODO 6) 개수를 1 늘리세요. (이걸 빼먹으면 큐가 망가진다)
        self.count += 1

        print(
            f'Enqueue({item}) -> {self.items} | front:{self.front}, rear:{self.rear}, count:{self.count}'
        )

    def dequeue(self):
        if self.is_empty():
            print('Queue is Empty!')
            return None

        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity  # front 순환 이동

        # TODO 7) 개수를 1 줄이세요.
        self.count -= 1

        print(
            f'Dequeue() -> {item} | {self.items} | front:{self.front}, rear:{self.rear}, count:{self.count}'
        )
        return item


print('=== count 방식 원형 큐 테스트 (크기 3, 3칸 모두 사용) ===')
cqf = CircularQueueFull(3)
cqf.enqueue('A')
cqf.enqueue('B')
cqf.enqueue('C')  # 3개 모두 저장 (공간 낭비 없음)
cqf.enqueue('D')  # Full
print()
cqf.dequeue()
cqf.enqueue('D')

# [비교] 두 방식의 트레이드오프
#   1칸 비우기 : 변수 하나 덜 쓰지만 공간 1칸을 버린다. 조건식이 다소 헷갈린다.
#   count 방식 : 공간을 다 쓰고 조건식이 직관적이지만, 관리할 상태가 하나 늘어난다.
#                (enqueue/dequeue 마다 count 갱신을 빼먹으면 조용히 망가진다)


print('\n' + '=' * 66 + '\n')


# ------------------------------------------------------------
# [스스로 점검하기]
# ------------------------------------------------------------
# Q1. TODO 1 에서 capacity + 1 을 하지 않으면 어떤 문제가 생길까? 공백과 포화를 무엇으로 구분할 수 있을까?
#       공백과 포화가 모두 front == rear 가 되어 구분이 불가능해진다.
#       "3개 넣고 싶으면 배열은 4칸" 을 기억할 것.
#
# Q2. % 를 빼고 그냥 rear += 1 로 쓰면 배열 끝에서 무슨 일이 일어날까?
#       배열 끝에서 IndexError 가 나거나, 순환이 안 돼서 원형 큐가 아니게 된다.
#
# Q3. is_full 을 선형 큐처럼 rear == capacity - 1 로 쓰면 원형 큐의 장점이 남아 있을까?
#      선형 큐의 조건을 그대로 가져온 실수. 원형 큐에서는 (rear + 1) % capacity == front 로 판단해야 한다.
#
