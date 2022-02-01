from operator import contains
from types import new_class
from code_challenges.trees.binary_trees import BinaryTree
from code_challenges.trees.node import Node

class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
         self.root = root


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

        if self.root is None:
            return False
        if self.root.value == value:
            return True

        if value < self.root.value:
            return contains(self.root.left, value)
        else:
            return contains(self.root.right, value)
            #return contains(self.root, value)

    def find_maximum_value(self):

        def find_max(root):
            _max = 0
            if root == None:
                return _max
            if _max < root.value:
                _max = root.value
            left_num = find_max(root.left, _max)
            if _max < left_num:
                _max = left_num

            right_num = find_max(root.right, _max)
            if _max < right_num:
                _max = right_num

            return _max
            

# if __name__ == "__main__":
#    bst = BinarySearchTree(Node(50))
#    bst.add(Node(40))
#    bst.add(Node(30))
#    bst.add(Node(45))
#    bst.add(Node(60))
#    bst.add(Node(55))
#    bst.add(Node(70))


#    print(bst.post_order)

#  def add(self, value):

#         def find_and_add(root, value):
#             new_node = Node(value)
#             if self.root is None:
#                 self.root = new_node
#                 #return

#             if root.value < new_node.value:
#                 if root.right:
#                     find_and_add(root.right, value)
#                 else:
#                     root.right = new_node

#             if self.root > new_node.value:
#                 if root.left:
#                     find_and_add(root.left, value)
#                 else:
#                     root.left = new_node

#             find_and_add(self.root, value)
