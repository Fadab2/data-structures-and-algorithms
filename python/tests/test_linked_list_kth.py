from code_challenges.linked_list_kth.linked_list_kth import Node, LinkedList

def test_find_k_greater_than_lenth():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.find_kth_value(5)
    expected = "Invalid input"
    assert actual == expected


def test_find_k_and_length_are_same():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.find_kth_value(4)
    expected = 1
    assert actual == expected


def test_find_k_negative():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.find_kth_value(-1)
    expected = "Invalid input"
    assert actual == expected


def test_find_k_in_lenght_one():
    ll = LinkedList()
    ll.insert(2)
    actual = ll.find_kth_value(0)
    expected = 2
    assert actual == expected


def test_find_k_in_the_middle():
    ll = LinkedList()
    ll.insert(4)
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)

    actual = ll.find_kth_value(2)
    expected = 8
    assert actual == expected
