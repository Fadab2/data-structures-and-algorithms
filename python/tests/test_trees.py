from operator import contains
import pytest
from code_challenges.trees.node import Node
from code_challenges.trees.binary_trees import BinaryTree
from code_challenges.trees.binary_search_tree import BinarySearchTree

def test_new_node():
    node = Node(11)
    actual = node.value
    expected = 11
    assert actual == expected


def test_new_node_bad():
    node = Node(11)
    actual = node.value
    expected = 12
    assert actual != expected


def test_bt_empty():
    bt = BinaryTree()
    assert bt


def test_bt_empty_root_none():
    bt = BinaryTree()
    assert bt.root == None


def test_traverse_pre_order():

    #           seattle
    #       /           \
    #   portland          vancouver

    seattle = Node('seattle')
    portland = Node('portland')
    vancouver = Node('vancouver')

    bt = BinaryTree(seattle)
    seattle.left = portland
    seattle.right = vancouver

    assert seattle.left == bt.root.left
    assert seattle.right == vancouver
    order_list = bt.pre_order()
    assert order_list == ['seattle', 'portland', 'vancouver']


def test_traverse_in_order():

    #           seattle
    #       /           \
    #   portland          vancouver

    seattle = Node('seattle')
    portland = Node('portland')
    vancouver = Node('vancouver')

    bt = BinaryTree(seattle)
    seattle.left = portland
    seattle.right = vancouver

    assert seattle.left == bt.root.left
    assert seattle.right == vancouver
    order_list = bt.in_order()
    assert order_list == ['portland', 'seattle', 'vancouver']


def test_traverse_post_order():

    #           seattle
    #       /           \
    #   portland          vancouver

    seattle = Node('seattle')
    portland = Node('portland')
    vancouver = Node('vancouver')

    bt = BinaryTree(seattle)
    seattle.left = portland
    seattle.right = vancouver

    assert seattle.left == bt.root.left
    assert seattle.right == vancouver
    order_list = bt.post_order()
    assert order_list == ['portland', 'vancouver', 'seattle']

#@pytest.mark.skip(reason="")
def test_binary_search_tree_pre_order():
    # add 50, 40,60,30,55,70,45
    #              50
    #           /      \
    #        40          60
    #       /   \       /   \
    #     30     45     55   70
    #

    bst = BinarySearchTree()
    bst.add(50)
    bst.add(40)
    bst.add(30)
    bst.add(45)
    bst.add(60)
    bst.add(55)
    bst.add(70)

    order_list = bst.pre_order()
    assert order_list == [50,40,30,45,60,55,70]


def test_binary_search_tree_in_order():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(40)
    bst.add(30)
    bst.add(45)
    bst.add(60)
    bst.add(55)
    bst.add(70)

    order_list = bst.in_order()
    assert order_list == [30,40,45,50,55,60,70]


def test_binary_search_tree_post_order():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(40)
    bst.add(30)
    bst.add(45)
    bst.add(60)
    bst.add(55)
    bst.add(70)

    order_list = bst.post_order()
    assert order_list == [30,45,40,55,70,60,50]


def test_binary_search_tree_contains_root():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(40)
    bst.add(30)
    bst.add(45)
    bst.add(60)
    bst.add(55)
    bst.add(70)

    assert bst.contains(50) == True

def test_binary_search_tree_contains_left_leaf():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(40)
    bst.add(30)
    bst.add(45)
    bst.add(60)
    bst.add(55)
    bst.add(70)
    assert bst.contains(45) == True


def test_binary_search_tree_contains_right_leaf():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(40)
    bst.add(30)
    bst.add(45)
    bst.add(60)
    bst.add(55)
    bst.add(70)
    assert bst.contains(70) == True
