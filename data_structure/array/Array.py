class Array:
    def __init__(self, length):
        self.__items = [0] * length

    def print(self):
        for i in self.__items:
            print(i)


array = Array(10)

array.print()
