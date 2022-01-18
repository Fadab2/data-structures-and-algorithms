from typing import Deque
from code_challenges.stack_and_queue.stack import Stack

class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack2.isEmpty() or self.stack1.isEmpty():
             print("Stack is empty")
             
        elif not self.stack1.isEmpty() and self.stack2.isEmpty():
            while self.stack1:
                item = self.stack1.pop()
                self.stack2.push(item)
            return self.stack2.pop()


if __name__ == "__main__":
    que = PseudoQueue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)

    print(que.dequeue())



