from data_structure.queue.Queue import Queue
from data_structure.stack.Stack import Stack
from data_structure.tree.Tree import Tree
from data_structure.linkedlist.LinkedList import LinkedList

tree = Tree()
tree.insert(8)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(10)
tree.insert(14)
tree.insert(13)


print(tree.count_leaves())

