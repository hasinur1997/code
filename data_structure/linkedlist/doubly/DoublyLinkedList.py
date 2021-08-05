from data_structure.linkedlist.doubly.Node import Node


# Class Doubly Linked List
class DoublyLinkedList:
    # Initialize
    def __init__(self):
        self.head = None
        self.tail = None

    # Add node at the top of the linked list
    def add_first(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node

    # Add node at the bottom of the linked list
    def add_last(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.tail
            new_node.prev = temp
            self.tail = new_node

    # Display the linked list
    def display(self):
        if self.is_empty():
            print("List is empty")
            return

        current = self.tail
        while current is not None:
            print(current.data)
            current = current.prev

    # Check the is not empty or not
    def is_empty(self):
        return self.head is None
