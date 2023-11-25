class CircularQueue:

    def __init__(self, size):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return self.front == self.rear and self.front != -1

    def is_empty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.is_full():
            return False

        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % len(self.queue)

        self.queue[self.rear] = data
        return True

    def dequeue(self):
        if self.is_empty():
            return False

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.queue)

        return self.queue[self.front]

    def size(self):
        if self.is_empty():
            return 0

        if self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return len(self.queue) - (self.rear - self.front) - 1

    def display(self):
        if self.is_empty():
            return

        if self.front <= self.rear:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, len(self.queue)):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")


if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    print("The size of the queue is:", cq.size())
    print("The front element is:", cq.dequeue())
    print("The rear element is:", cq.dequeue())
    print("The size of the queue is:", cq.size())
    cq.enqueue(6)
    cq.enqueue(7)
    print("The size of the queue is:", cq.size())
    cq.display()