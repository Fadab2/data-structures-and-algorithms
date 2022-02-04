from code_challenges.stack_and_queue.node import Node
import sys


class Queue:
    def __init__(self, front=None):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            deq_node = self.front
            self.front = self.front.next
            return deq_node

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.front.value

    def isEmpty(self):
        if self.front == None:
            return True

        return False

    def __str__(self):
        if self.isEmpty():
            print("Queue is empty")

        else:
            current = self.front
            queue = " "

            while(current):
                queue += (f'{{ {current.value} }} -> ')
                current = current.next
            queue = (f'{queue}NULL')
            return queue


if __name__ == "__main__":
    que1 = Queue()
    que1.enqueue(1)
    que1.enqueue(2)
    que1.enqueue(3)
    que1.enqueue(4)

    print(str(que1.rear.value))
    print(str(que1.front.value))

    que1.dequeue()
    que1.dequeue()
    # print(str(que1.rear.value))
    # print(str(que1.front.value))

    print(que1.peek())
    print(que1.__str__())
