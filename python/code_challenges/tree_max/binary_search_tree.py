from operator import contains
from types import new_class
from code_challenges.trees.binary_trees import BinaryTree
from code_challenges.trees.node import Node

class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
         self.root = root
         self._max = 0


    def add(self, value):
            new_node = Node(value)
            current = self.root
            if current is None:
                self.root = new_node
                #return
            while current:

                if value > current.value:
                    if current.right == None:
                        current.right = new_node
                        return self
                    current = current.right
                else:
                    if current.left == None:
                        current.left = new_node
                        return self
                    current = current.left

    def contains(self, value):

        def find_value(root, value):
            if root is None:
                return False
            if root.value == value:
                return True

            if value < root.value:
                return find_value(root.left, value)

            if value > root.value:
                return find_value(root.right, value)

        return find_value(self.root, value)


    def find_maximum_value(self):

        def find_max(root):

            if root == None:
                return self._max
            # if _max < root.value:
            #     _max = root.value
            # find_max(root.left)


            if self._max < self.root.value:
                self._max = root.value
            find_max(root.left, self._max)

            if self._max < root.value:
                self._max = root.value
            find_max(root.right, self._max)
            return self._max

        find_max(self.root)
        return self._max
