def mychu_simulation(total_candy):
    queue = [(1, 1)]

    last_student = 0
    next_student = 2

    while total_candy > 0:
        student_id, want = queue.pop(0)

        give = min(want, total_candy)
        total_candy -= give
        last_student = student_id

        if total_candy == 0:
            break

        queue.append((student_id, want + 1))

        queue.append((next_student, 1))
        next_student += 1
    return last_student

print(mychu_simulation(20))

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full")
            return None
        self.rear += 1
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        self.front += 1
        item = self.items[self.front]
        self.items[self.front] = None

    def peek(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        return self.items[self.front + 1]

    def get_size(self):
        return self.rear - self.front

q = LinearQueue(4)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.dequeue()
q.dequeue()

print(q.get_size())
print(q.peek())
print(q.items)

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.items = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return None

        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        self.front = (self.front + 1) % self.capacity
        item = self.items[self.front]
        self.items[self.front] = None
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        return self.items[(self.front + 1) % self.capacity]

    def get_size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

cq = CircularQueue(3)
print(cq.items)
cq.enqueue('a')
cq.enqueue('b')
cq.enqueue('c')
print(cq.items)
cq.enqueue('d')

cq.dequeue()
print(cq.items)
cq.enqueue('D')
print(cq.items)

from collections import deque
dq = deque([10, 20, 30])

dq.append(40)
dq.appendleft(0)
right_item = dq.pop()
print(dq)
left_item = dq.popleft()
print(dq)

dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)
print(dq)
dq.rotate(-1)
print(dq)

dq2 = deque([1,2,3,4,5])
for _ in range(2):
    dq2.appendleft(dq2.pop())

print(dq2)

dq3 = deque([1,2,3,4,5])

for _ in range(2):
    dq3.append(dq3.popleft())

print(dq3)

recent = deque(maxlen=3)
for value in [1,2,3,4,5]:
    recent.append(value)
    print(recent)

print("=====" *5)


print("데큐")
from collections import deque
my_q = deque()
my_q.append(1)
my_q.append(2)
my_q.append(3)

print(my_q.popleft())
print(my_q.popleft())
print(my_q.popleft())


print("원형큐")
class circleque:
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.items = [None] * self.capacity
        self.rear = 0
        self.front = 0

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("찼다")
            return None

        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("없어")
            return None
        self.front = (self.front + 1) % self.capacity
        item = self.items[self.front]
        self.items[self.front] = None
        return item


my_cq = circleque(3)
my_cq.enqueue(1)
my_cq.enqueue(2)
my_cq.enqueue(3)

print(my_cq.dequeue())
print(my_cq.dequeue())
print(my_cq.dequeue())

print("리스트")
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list.pop(0))
print(my_list.pop(0))
print(my_list.pop(0))