from abc import abstractclassmethod
from code_challenges.linked_list_zip.linked_list_zip import Node, LinkedList


def test_zip_equal_ll():
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(3)
    ll1.insert(2)

    ll2 = LinkedList()
    ll2.insert(5)
    ll2.insert(9)
    ll2.insert(4)
    ll3 = ll1.zip_lists(ll1, ll2)
    assert ll3.__str__() == " { 2 } -> { 4 } -> { 3 } -> { 9 } -> { 1 } -> { 5 } -> NULL"


def test_zip_first_ll_greater():
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(3)
    ll1.insert(2)
    ll1.insert(6)
    ll1.insert(7)

    ll2 = LinkedList()
    ll2.insert(5)
    ll2.insert(9)
    ll2.insert(4)
    ll3 = LinkedList()
    #ll1.zip_lists(ll1, ll2)
    ll3 = ll1.zip_lists(ll1, ll2)
    actual = ll3.__str__()
    expected = " { 7 } -> { 4 } -> { 6 } -> { 9 } -> { 2 } -> { 5 } -> { 3 } -> { 1 } -> NULL"
    assert actual == expected


def test_zip_second_ll_greater():
    ll3 = LinkedList
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(3)
    ll1.insert(2)

    ll2 = LinkedList()
    ll2.insert(5)
    ll2.insert(9)
    ll2.insert(4)
    ll2.insert(6)
    ll2.insert(7)
    ll3 = ll1.zip_lists(ll1, ll2)
    assert ll3.__str__() == " { 2 } -> { 7 } -> { 3 } -> { 6 } -> { 1 } -> { 4 } -> { 9 } -> { 5 } -> NULL"

def test_zip_empty_ll():
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(3)
    ll1.insert(2)

    ll2 = LinkedList()
    ll3 = ll1.zip_lists(ll1, ll2)
    assert ll3.__str__() == " { 2 } -> { 3 } -> { 1 } -> NULL"
