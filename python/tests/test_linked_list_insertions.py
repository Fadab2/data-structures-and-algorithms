from code_challenges.linked_list_insertions.linked_list_insertions import Node, LinkedList
import pytest

# Can successfully add a node to the end of the linked list
def test_append_add_node():
    ll = LinkedList()
    ll.append(10)
    actual =  ll.head.value
    expected = 10
    assert actual == expected

# Can successfully add multiple nodes to the end of a linked list
def test_append_add_multiple_nodes():
    ll = LinkedList()
    ll.append(10)
    ll.append(12)
    ll.append(15)
    actual = ll.__str__()
    expected = " { 10 } -> { 12 } -> { 15 } -> NULL"
    assert actual == expected

# Can successfully insert a node before a node located i the middle of a linked list
def test_insert_before_value_not_in_list():
    ll = LinkedList()
    ll.append('1')
    ll.append('3')
    ll.append('2')
    ll.insert_before('3','5')
    acutal =  ll.__str__()
    expected = " { 1 } -> { 5 } -> { 3 } -> { 2 } -> NULL"
    assert acutal == expected

# Can successfully display an error message if the value does not exist linked list
def test_insert_before_value_exist():
    ll = LinkedList()
    ll.append('1')
    ll.append('3')
    ll.append('2')
    actual = ll.insert_before('4','5')
    expected = "Error: the node with specified value is not in the linked list"
    assert actual == expected

# Can successfully insert a node before the first node of a linked list
def test_insert_before_first_node_in_list():
    ll = LinkedList()
    ll.append('1')
    ll.append('3')
    ll.append('2')
    ll.insert_before('1','5')
    acutal =  ll.__str__()
    expected = " { 5 } -> { 1 } -> { 3 } -> { 2 } -> NULL"
    assert acutal == expected

# Can successfully insert after a node in the middle of the linked list
def test_insert_after_node_in_list():
    ll = LinkedList()
    ll.append('1')
    ll.append('2')
    ll.append('2')
    ll.insert_after('2','5')
    acutal =  ll.__str__()
    expected = " { 1 } -> { 2 } -> { 5 } -> { 2 } -> NULL"
    assert acutal == expected

# Can successfully insert a node after the last node of the linked list
def test_insert_at_end_of_list():
    ll = LinkedList()
    ll.append('1')
    ll.append('2')
    ll.append('3')
    ll.insert_after('3','4')
    acutal =  ll.__str__()
    expected = " { 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL"
    assert acutal == expected
