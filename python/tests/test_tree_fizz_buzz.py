from code_challenges.tree_fizz_buzz.tree_fizz_buzz import K_AryTree, Node

import pytest

#@pytest.mark.skip(reason="")
def test_empty_tree():
    empty_tree = K_AryTree()
    assert empty_tree.root == None



def test_kary_tree_fizz_buzz_one_node():
    ktree = K_AryTree()
    ktree.root = Node(10)
    assert ktree.root.value == 10


@pytest.mark.skip(reason="")
def test_kary_tree_test_fizz():
    ktree = K_AryTree()
    ktree = Node(3)
    assert ktree.children == ['Fizz']


@pytest.mark.skip(reason="")
def test_kary_tree_test_buzz():
    ktree = K_AryTree()
    ktree = Node(5)
    assert ktree.children == ['Buzz']


@pytest.mark.skip(reason="")
def test_kary_tree_test_fizzbuzz():
    ktree = K_AryTree()
    ktree = Node(15)
    assert ktree.children == ['FizzBuzz']


@pytest.mark.skip(reason="")
def test_kary_tree_test_many_nodes():
    ktree = K_AryTree()
    ktree = Node(4)
    ktree = Node(15)
    ktree = Node(50)
    ktree = Node(9)
    ktree = Node(5)
    assert ktree.children == ['4','FizzBuzz','50','Fizz','Buzz']
