class HashTable:
    def __init__(self, length=5):
        self.items = [None] * length

    def add(self, key, value):
        index = self.hash(key)

        if self.items is not None:
            for i in self.items[index]:
                if i[0] == key:
                    i[i] = value
                    break
            else:
                self.items[index].append([key, value])

        else:
            self.items[index] = []
            self.items[index].append([key, value])

    def hash(self, key):
        return hash(key) % len(self.items)
