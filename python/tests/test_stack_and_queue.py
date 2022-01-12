from code_challenges.stack_and_queue.queue import Queue
from code_challenges.stack_and_queue.stack import Stack


def test_push_one_item():
    stack = Stack()
    stack.push(1)

    actual = stack.__str__()
    expected = " { 1 } -> NULL"

    assert actual == expected

def test_push_multiple_items():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    actual = stack.__str__()
    expected = " { 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected

def test_pop_one_item():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()

    actual = stack.__str__()
    expected = " { 3 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected

def test_pop_all_items():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()

    assert stack.isEmpty()==True

def test_peek_next_items():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    assert stack.peek()== 4

def test_instantiate_empty_stack():
    stack = Stack()

    assert stack.peek()== None

def test_instantiate_empty_stack():
    stack = Stack()
    stack.pop()
    assert stack.isEmpty() == True

#Can successfully enqueue into a queue
def test_enqueue_into_queue():
    que1 = Queue()
    que1.enqueue(1)

    actual = que1.__str__()
    expected = " { 1 } -> NULL"

    assert actual == expected

def test_enqueue_multiple_items():
    que1 = Queue()
    que1.enqueue(1)
    que1.enqueue(2)
    que1.enqueue(3)
    actual = que1.__str__()
    expected = " { 1 } -> { 2 } -> { 3 } -> NULL"

    assert actual == expected

def test_dequeue_one_items():
    que1 = Queue()
    que1.enqueue(1)
    que1.enqueue(2)
    que1.enqueue(3)
    que1.dequeue()

    actual = que1.__str__()
    expected = " { 2 } -> { 3 } -> NULL"

    assert actual == expected

def test_peek_into_queue():
    que1 = Queue()
    que1.enqueue(1)
    que1.enqueue(2)
    que1.enqueue(3)


    assert que1.peek() == 1

def test_dequeue_till_empty():
    que1 = Queue()
    que1.enqueue(1)
    que1.enqueue(2)
    que1.enqueue(3)
    que1.dequeue()
    que1.dequeue()
    que1.dequeue()

    assert que1.isEmpty() == True

def test_instantiate_empty_queue():
    que1 = Queue()

    assert que1.isEmpty() == True

def test_dequeue_peek_on_empty():
    que1 = Queue()
    que1.enqueue(1)
    que1.enqueue(2)
    que1.enqueue(3)
    que1.dequeue()
    que1.dequeue()
    que1.dequeue()

    assert que1.peek() == None
    assert que1.dequeue() == None

