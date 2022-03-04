
from code_challenges.trees.node import Node
# from code_challenges.trees.binary_trees import BinaryTree
import pytest
from code_challenges.trees.binary_search_tree import BinarySearchTree

from code_challenges.stack_and_queue.queue import Queue
from code_challenges.tree_breadth_first.tree_breadth_first import breadth_frist

@pytest.mark.skip(reason="")
def test_binary_search_tree_in_order():
    bst = BinarySearchTree(3)
    node1 = Node(2)
    node2 = Node(5)
    node3 = Node(10)
    node4 = Node(20)
    node5 = Node(33)
    node6 = Node(15)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6

    order_list = bst.breadth_first()
    assert order_list == [2, 5, 10, 20, 33, 15]
