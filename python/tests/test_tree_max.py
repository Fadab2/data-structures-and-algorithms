import pytest
from code_challenges.trees.node import Node
from code_challenges.trees.binary_trees import BinaryTree
from code_challenges.trees.binary_search_tree import BinarySearchTree
from code_challenges.tree_max.binary_search_tree import BinarySearchTree


@pytest.mark.skip(reason="")
def test_find_max_when_empty():
    bst = BinarySearchTree()
    assert bst.find_maximum_value() == 0


@pytest.mark.skip(reason="")
def test_find_max_when_first_node():
    bst = BinarySearchTree(50)
    node1 = Node(50)
    node2 = Node(40)
    node3 = Node(30)

    node1.left = node2
    node1.right = node3

    max_value = bst.find_maximum_value()
    assert max_value == 50


@pytest.mark.skip(reason="")
def test_find_max_when_left_child():
    bst = BinarySearchTree(50)
    node1 = Node(50)
    node2 = Node(60)
    node3 = Node(30)

    node1.left = node2
    node1.right = node3

    max_value = bst.find_maximum_value()
    assert max_value == 60


@pytest.mark.skip(reason="")
def test_find_max__when_right_child():
    bst = BinarySearchTree(50)
    node1 = Node(50)
    node2 = Node(60)
    node3 = Node(70)

    node1.left = node2
    node1.right = node3

    max_value = bst.find_maximum_value()
    assert max_value == 70


@pytest.mark.skip(reason="")
def test_find_max_when_two_max_numbers():
    bst = BinarySearchTree(3)
    node1 = Node(3)
    node2 = Node(10)
    node3 = Node(25)
    node4 = Node(8)
    node5 = Node(11)
    node6 = Node(25)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6

    max_value = bst.find_maximum_value()
    assert max_value == 25


# def test_find_max_when_left_child():
#     bst = BinarySearchTree()
#     bst.add(20)
#     bst.add(40)
#     bst.add(30)
#     assert bst.find_maximum_value() == 50

