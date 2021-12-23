from code_challenges.linked_list.linked_list import Node, LinkedList
import pytest

def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1


def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2

def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node

def test_linked_list_empty():
    ll = LinkedList()
    assert ll.head == None

def test_insert_to_empty_linked_list():
    # ll.head = apple
    ll = LinkedList()
    ll.insert('a')
    assert ll.head.value == 'a'

# returns returns if a value exist in the linked list
def test_includes_to_return_true():
    ll = LinkedList()
    ll.insert('c')
    assert ll.includes('c') == True

# returns false for a value that doesn't exist in the linked list
def test_includes_to_return_false():
    ll = LinkedList()
    assert ll.includes('d') != True
