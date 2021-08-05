from data_structure.tree.Node import Node


# Class Tree
class Tree:
    # Initialize
    def __init__(self):
        self.root = None
        self.size = 0

    # Insert item
    def insert(self, item):
        new_node = Node(item)

        if self.root is None:
            self.root = new_node
            self.size += 1
            return

        current_node = self.root
        while True:
            if item < current_node.data:
                if current_node.left is None:
                    current_node.left = new_node
                    self.size += 1
                    break
                current_node = current_node.left

            else:
                if current_node.right is None:
                    current_node.right = new_node
                    self.size += 1
                    break
                current_node = current_node.right

    # Check item is exists in tree or not
    def find(self, item):
        current = self.root

        while current is not None:
            if item < current.data:
                current = current.left
            elif item > current.data:
                current = current.right
            else:
                return True

        return False


    def traverse_in_order(self):
        self.__traverse_in_order(self.root)

    def __traverse_in_order(self, root):
        if root is None:
            return
        self.__traverse_in_order(root.left)
        print(root.data)
        self.__traverse_in_order(root.right)

    def traverse_pre_order(self):
        self.__traverse_pre_order(self.root)

    def __traverse_pre_order(self, root):
        if root is None:
            return
        print(root.data)
        self.__traverse_pre_order(root.left)
        self.__traverse_pre_order(root.right)

    def traverse_post_order(self):
        self.__traverse_post_order(self.root)

    def __traverse_post_order(self, root):
        if root is None:
            return
        self.__traverse_post_order(root.left)
        self.__traverse_post_order(root.right)
        print(root.data)

    def height(self):
        return self.__height(self.root)

    def __height(self, root):
        if root is None:
            return 0
        left_height = 0
        right_height = 0

        if root.left is not None:
            left_height = 1 + self.__height(root.left)

        if root.right is not None:
            right_height = 1 + self.__height(root.right)

        return max(left_height, right_height)

    def length(self):
        return self.size

    def print_node_at_distance(self, distance):
        self.__print_node_at_distance(self.root, distance)

    def __print_node_at_distance(self, root, distance):
        if root is None:
            return
        if distance == 0:
            print(root.data)
            return
        self.__print_node_at_distance(root.left, distance - 1)
        self.__print_node_at_distance(root.right, distance - 1)

    def contains(self, item):
        return self.__check_item(self.root, item)

    def __check_item(self, root, item):
        if root is None:
            return False
        if item == root.data:
            return True

        if item < root.data:
            return self.__check_item(root.left, item)
        else:
            return self.__check_item(root.right, item)

    def are_siblings(self, item1, item2):
        print(self.__check_siblings(self.root, item1, item2))

    def __check_siblings(self, root, item1, item2):
        if root is None:
            return False

        if root.left is None or root.right is None:
            return False
        if (root.left == item1 or root.right == item1) and (root.left == item2 or root.right == item2):
            return True
        self.__check_siblings(root.left, item1, item2)
        self.__check_siblings(root.right, item1, item2)

    def max(self):
        print(self.__get_max(self.root))

    def __get_max(self, root):
        if root is None:
            return 0

        max_value = root.data
        left_child_value = self.__get_max(root.left)
        right_child_value = self.__get_max(root.right)

        if max_value < left_child_value:
            max_value = left_child_value

        if max_value < right_child_value:
            max_value = right_child_value

        return max_value

    def count_leaves(self):
        return self.__count_leaves(self.root)

    def __count_leaves(self, root):
        if root is None:
            return 0

        if self.__is_leaf(root):
            return 1

        return self.__count_leaves(root.left) + self.__count_leaves(root.right)

    def __is_leaf(self, node):
        return node.left is None and node.right is None


    def is_empty(self):
        return self.root is None
