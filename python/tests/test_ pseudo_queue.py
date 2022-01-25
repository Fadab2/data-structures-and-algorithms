from code_challenges.stack_queue_pseudo.pseudo_queue import PseudoQueue
import pytest

# Can successfully enqueue into a queue
@pytest.mark.skip(reason="")
def test_enqueue_into_queue():
    que1 = PseudoQueue()
    que1.enqueue(1)

    actual = que1.__str__()
    expected = " { 1 } -> NULL"

    assert actual == expected


# Can successfully enqueue multiple items
@pytest.mark.skip(reason="")
def test_enqueue_multiple_items():
    que1 = PseudoQueue()
    que1.enqueue(1)
    que1.enqueue(2)
    que1.enqueue(3)
    actual = que1.__str__()
    expected = " { 1 } -> { 2 } -> { 3 } -> NULL"

    assert actual == expected


# Can successfully dequeue an item
@pytest.mark.skip(reason="")
def test_dequeue_one_items():
    que1 = PseudoQueue()
    que1.enqueue(1)
    que1.enqueue(2)
    que1.enqueue(3)
    que1.dequeue()

    actual = que1.__str__()
    expected = " { 2 } -> { 3 } -> NULL"

    assert actual == expected


# Can successfully dequeue multiple items
@pytest.mark.skip(reason="")
def test_dequeue_multiple_items():
    que1 = PseudoQueue()
    que1.enqueue(1)
    que1.enqueue(2)
    que1.enqueue(3)
    que1.dequeue()
    que1.dequeue()

    actual = que1.__str__()
    expected = " { 1 } -> NULL"

    assert actual == expected


# Can successull return empty if stack is empty
@pytest.mark.skip(reason="")
def test_dequeue_empty_stack():
    que1 = PseudoQueue()
    que1.dequeue()

    actual = que1.__str__()
    expected = "Stack is empty"

    assert actual == expected
