
from code_challenges.stack_and_queue.stack import Stack

class PseudoQueue:
    def __init__(self, top=None):
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
                return
        else:
            while not self.stack1.isEmpty:
                item = self.stack1.pop()
                self.stack2.push(item)
                return_value = self.stack2.pop()
            return return_value

    # a methoded to print string representation of the elements
    def __str__(self):
        if self.stack2.isEmpty() or self.stack1.isEmpty():
             print("Stack is empty")

        else:
            current = self.top
            stack = " "

            while(current):
                stack += (f'{{ {current.value} }} -> ')
                current = current.next
            stack = (f'{stack}NULL')
            return stack


if __name__ == "__main__":
    que = PseudoQueue()
    que.enqueue(10)
    que.enqueue(15)
    que.enqueue(20)
    que.enqueue(20)


    que.__str__()

