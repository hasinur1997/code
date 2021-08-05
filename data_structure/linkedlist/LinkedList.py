from data_structure.linkedlist.Node import Node

# Class Linked List


class LinkedList:
    # Initialize
    def __init__(self):
        self.first = None
        self.last = None
        self.__size = 0

    # Add node on first
    def add_first(self, data):
        new_node = Node(data)

        if self.__is_empty():
            self.first = self.last = new_node
        else:
            current_node = self.first
            self.first = new_node
            new_node.next = current_node
        self.__size += 1

    # Add node on last
    def add_last(self, data):
        new_node = Node(data)

        if self.__is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.__size += 1

    def index_of(self, item):
        index = 0
        current_node = self.first

        while current_node is not None:
            if current_node.data == item:
                return index
            current_node = current_node.next
            index = index + 1

        return -1

    def contains(self, item):
        return self.index_of(item) != -1

    def remove_first(self):
        if self.__is_empty():
            print("The list is empty, nothing to delete")
            exit()

        if self.first == self.last:
            return None

        self.first = self.first.next
        self.__size -= 1

    def remove_last(self):
        prev = self.get_previous(self.last)

        prev.next = None
        self.last = prev
        self.__size -= 1

    def to_array(self):
        current_node = self.first
        data = []

        while current_node is not None:
            data.append(current_node.data)
            current_node = current_node.next

        return data

    def reverse(self):
        if self.__is_empty():
            return
        previous = self.first
        current = previous.next

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.last = self.first
        self.last.next = None
        self.first = previous

    def get_kth_node_from_end(self, k):
        if self.__is_empty():
            return -1
        index = 0
        current = self.first

        while current is not None:
            if k == index:
                break
            current = current.next
            index += 1
        return current.data

    def get_previous(self, node):
        if self.__is_empty():
            print("The list is empty, nothing to delete")
            exit()

        current_node = self.first

        while current_node is not None:
            if current_node.next == node:
                return current_node
            current_node = current_node.next

        return None

    def sort(self):
        if self.first is None:
            return False

        current = self.first

        while current is not None:
          target = current.next
          while target is not None:
              if current.data > target.data:
                  temp = current.data
                  current.data = target.data
                  target.data = temp
              target = target.next
          current = current.next

    def size(self):
        return self.__size

    def __is_empty(self):
        return self.first is None

    # Print the list
    def print(self):

        if self.first is None:
            print("The list is empty.")
        else:
            current_node = self.first
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next
