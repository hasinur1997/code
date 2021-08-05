class Stack:
    def __init__(self, size):
        self.size = size
        self.items = []
        self.top = 0

    def push(self, item):
        if self.is_full():
            raise Exception("Sorry, Stack overflow")

        self.items.insert(self.top, item)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Underflow")

        item = self.items[self.get_top()]
        del self.items[self.get_top()]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is underflow")
        return self.items[self.get_top()]

    def is_full(self):
        return self.top == self.size

    def is_empty(self):
        return len(self.items) == 0

    def get_top(self):
        return self.top - 1

