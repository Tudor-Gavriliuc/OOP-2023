from abc import ABC, abstractmethod
from collections import deque


class Queue(ABC):
    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass


class ListQueue(Queue):
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise Exception("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise Exception("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


class TwoStackQueue(Queue):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.is_empty():
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            raise Exception("Queue is empty")

    def peek(self):
        if not self.is_empty():
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        else:
            raise Exception("Queue is empty")

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)


list_queue = ListQueue()
list_queue.enqueue("lion")
list_queue.enqueue("tiger")
list_queue.enqueue("elephant")

# Check if the ListQueue is empty and peek at the front animal
print("Is the ListQueue empty?", list_queue.is_empty())
print("Front animal of ListQueue:", list_queue.peek())

# Dequeue animals from the ListQueue and show the dequeued animals
print("Dequeued animal from ListQueue:", list_queue.dequeue())
print("Dequeued animal from ListQueue:", list_queue.dequeue())
print("Dequeued animal from ListQueue:", list_queue.dequeue())

# Check if the ListQueue is empty again
print("Is the ListQueue empty?", list_queue.is_empty())

# Create a TwoStackQueue and enqueue some fruits
two_stack_queue = TwoStackQueue()
two_stack_queue.enqueue("apple")
two_stack_queue.enqueue("orange")
two_stack_queue.enqueue("banana")

# Check if the TwoStackQueue is empty and peek at the front fruit
print("Is the TwoStackQueue empty?", two_stack_queue.is_empty())
print("Front fruit of TwoStackQueue:", two_stack_queue.peek())

# Dequeue fruits from the TwoStackQueue and show the dequeued fruits
print("Dequeued fruit from TwoStackQueue:", two_stack_queue.dequeue())
print("Dequeued fruit from TwoStackQueue:", two_stack_queue.dequeue())
print("Dequeued fruit from TwoStackQueue:", two_stack_queue.dequeue())

# Check if the TwoStackQueue is empty again
print("Is the TwoStackQueue empty?", two_stack_queue.is_empty())