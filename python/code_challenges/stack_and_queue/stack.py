
from stack_and_queue.node import Node

class Stack:
    def __init__(self, top=None):
        self.top = None

    def push(self, value):

        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None

            return temp.value

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.top.value



    def __str__(self):
        if self.isEmpty():
             print("Stack is empty")
             exit(0)
        else:
            current = self.top
            stack = " "

            while(current):
                stack += (f'{{ {current.value} }} -> ')
                current = current.next
            stack = (f'{stack}NULL')
            return stack

    def isEmpty(self):
        if self.top == None:
            return True
        return False


if __name__ == "__main__":
    stack1 = Stack()

    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    print(stack1.__str__())
    stack1.pop()
    stack1.pop()
    stack1.pop()


    stack1.__str__()
    stack1.peek()
