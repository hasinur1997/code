class Queue:
    def __init__(self, size):
        self.front = 0
        self.rear = 0
        self.items = []
        self.size = size

    def add(self, item):
        if self.is_full():
            raise Exception("Queue is full")

        self.items.insert(self.rear, item)
        self.rear += 1

    def remove(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        item = self.items[self.front]
        del self.items[self.front]

        return item

    def peek(self):
        return self.items[self.front]

    def is_full(self):
        return self.rear == self.size

    def is_empty(self):
        return len(self.items) == 0
