from operator import contains
from types import new_class
from code_challenges.trees.binary_trees import BinaryTree
from code_challenges.trees.node import Node

class BinarySearchTree(BinaryTree):

    def add(self, value):

        def find_and_add(root, value):
            new_node = Node(value)
            if self.root is None:
                self.root = new_node

            if root.value < value:
                if root.right:
                    find_and_add(root.right, value)
                else:
                    root.right = new_node

            if self.root > value:
                if root.left:
                    find_and_add(root.left, value)
                else:
                    root.left = new_node
            else:
                find_and_add(self.root, value)



    def contains(self, value):
        if self.root is None:
            return False

        if self.root.value == value:
            return True

        if value < self.root.value:
            if self.root.left:
                contains(self.root.left, value)
                return True
        else:
            if self.root.right:
                contains(self.root.right, value)
                return True

        return False

