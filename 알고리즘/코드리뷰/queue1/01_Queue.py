my_que1 = []
my_que1.append(1)
my_que1.append(2)
my_que1.append(3)

a1 = my_que1.pop(0)
b1 = my_que1.pop(0)
c1 = my_que1.pop(0)

print(a1, b1, c1)



from collections import deque

my_que2 = deque([])

my_que2.append(1)
my_que2.append(2)
my_que2.append(3)

a1 = my_que2.popleft()
b1 = my_que2.popleft()
c1 = my_que2.popleft()

print(a1, b1, c1)

class CircularQueue:
    def __init__(self, n):
        self.capacity = n + 1
        self.items = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("찼습니다")
            return None

        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("비었어요")
            return None

        self.front = (self.front + 1) % self.capacity
        return self.items[self.front]

my_que3 = CircularQueue(3)

my_que3.enqueue(1)
my_que3.enqueue(2)
my_que3.enqueue(3)

print(my_que3.dequeue())
print(my_que3.dequeue())
print(my_que3.dequeue())