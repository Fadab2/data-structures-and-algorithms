
from code_challenges.animal_shelter.animal_shelter import AnimalShelter
import pytest

# Can successfully enqueue into a queue
#@pytest.mark.skip(reason="")
def test_enqueue_into_queue():
    que1 = AnimalShelter()
    que1.enqueue("cat")

    actual = que1.__str__()
    expected = " { cat } -> NULL"

    assert actual == expected


# Can successfully enqueue multiple items
#@pytest.mark.skip(reason="")
def test_enqueue_multiple_items():
    que1 = AnimalShelter()
    que1.enqueue("cat")
    que1.enqueue("dog")
    que1.enqueue("dog")
    que1.enqueue("cat")
    que1.enqueue("dog")

    actual = que1.__str__()
    expected = " { cat } -> { dog } -> { dog } -> { cat } -> { dog } -> NULL"

    assert actual == expected


# Can successfully dequeue an item if pref is first item
#@pytest.mark.skip(reason="")
def test_dequeue_when_pref_is_first_items():
    que1 = AnimalShelter()
    que1.enqueue("cat")
    que1.enqueue("dog")
    que1.enqueue("dog")
    que1.enqueue("cat")
    que1.enqueue("dog")

    que1.dequeue("cat")

    actual = que1.__str__()
    expected = " { dog } -> { dog } -> { cat } -> { dog } -> NULL"

    assert actual == expected


# Can successfully dequeue multiple items
#@pytest.mark.skip(reason="")
def test_dequeue_when_pref_is_not_first_items():
    que1 = AnimalShelter()
    que1.enqueue("dog")
    que1.enqueue("cat")
    que1.enqueue("cat")
    que1.enqueue("dog")

    que1.dequeue("cat")

    actual = que1.__str__()
    expected = " { cat } -> { dog } -> { dog } -> NULL"

    assert actual == expected


# Can successull return empty if stack is empty
@pytest.mark.skip(reason="")
def test_dequeue_empty_stack():
    que1 = AnimalShelter()
    que1.dequeue("cat")

    actual = que1.__str__()
    expected = "Queue is empty"

    assert actual == expected
