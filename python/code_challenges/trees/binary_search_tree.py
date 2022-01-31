from operator import contains
from types import new_class
from code_challenges.trees.binary_trees import BinaryTree
from code_challenges.trees.node import Node

class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)

    def add(self, value):

        def find_and_add(root, value):
            new_node = Node(value)
            if self.root is None:
                self.root = new_node
                return

            if root.value < new_node.value:
                if root.right:
                    find_and_add(root.right, value)
                else:
                    root.right = new_node

            if self.root > new_node.value:
                if root.left:
                    find_and_add(root.left, value)
                else:
                    root.left = new_node

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


if __name__ == "__main__":
   bst = BinarySearchTree(Node(50))
   bst.add(Node(40))
   bst.add(Node(30))
   bst.add(Node(45))
   bst.add(Node(60))
   bst.add(Node(55))
   bst.add(Node(70))


   print(bst.post_order)
