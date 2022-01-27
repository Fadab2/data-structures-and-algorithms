
from black import re
from code_challenges.stack_and_queue.stack import Stack

class PseudoQueue:
    def __init__(self):
        self.top = None
        self.stack1 = Stack()
        self.stack2 = Stack()

    # a method to push values in stack1
    def enqueue(self, value):
        self.stack1.push(value)
    # a method to add items popped out from stack1 into stack2 using push method and then return values when dequeue called
    def dequeue(self):
        if self.stack2.isEmpty():
            if self.stack1.isEmpty():
                print("Stack is empty")

        while not self.stack1.isEmpty():
            item = self.stack1.pop()
            self.stack2.push(item)
            #print("stack2: ", self.stack2)
        return_value = self.stack2.pop()
        return return_value

    # a methoded to print string representation of the elements
    def __str__(self):
        stack = " "
        if self.stack1.isEmpty():
            current = self.stack2.top

        if self.stack2.isEmpty():
            current = self.stack1.top
        if self.stack2.isEmpty() and self.stack1.isEmpty():
            empty = "Stack is empty"
            return empty
        while(current):
            stack += (f'{{ {current.value} }} -> ')
            current = current.next
        stack = (f'{stack}NULL')
        return stack



if __name__ == "__main__":
    que = PseudoQueue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.dequeue()

    print(que.__str__())

