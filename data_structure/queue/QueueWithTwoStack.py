from data_structure.stack.Stack import Stack


# Class QueueWithTwoStack
class QueueWithTwoStack:
    # Initialize
    def __init__(self, size):
        self.__stack1 = Stack(size)
        self.__stack2 = Stack(size)
        self.size = size
        self.counter = 0

    # Enqueue item in queue
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")

        self.__stack1.push(item)
        self.counter += 1

    # Dequeue item from queue
    def dequeue(self):
        self.__move_stack1_to_stack2()

        self.counter -= 1
        return self.__stack2.pop()

    # Check empty
    def is_empty(self):
        return self.__stack1.is_empty() and self.__stack2.is_empty()

    # Check queue is full
    def is_full(self):
        return self.size == self.counter

    # Peek item from the queue
    def peek(self):
        self.__move_stack1_to_stack2()
        return self.__stack2.peek()

    def __move_stack1_to_stack2(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        if self.__stack2.is_empty():
            while not self.__stack1.is_empty():
                self.__stack2.push(self.__stack1.pop())
