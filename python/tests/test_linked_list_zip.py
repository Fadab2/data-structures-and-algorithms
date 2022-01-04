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
    ll1.zip_lists(ll1, ll2)
    assert ll1.__str__() == " { 2 } -> { 4 } -> { 3 } -> { 9 } -> { 1 } -> { 5 } -> NULL"


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
    ll1.zip_lists(ll1, ll2)
    assert ll1.__str__() == " { 7 } -> { 4 } -> { 6 } -> { 9 } -> { 2 } -> { 5 } -> { 3 } -> { 1 } -> NULL"

def test_zip_empty_ll():
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(3)
    ll1.insert(2)

    ll2 = LinkedList()
    ll1.zip_lists(ll1, ll2)
    assert ll1.__str__() == " { 2 } -> { 3 } -> { 1 } -> NULL"
