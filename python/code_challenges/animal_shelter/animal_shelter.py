from code_challenges.stack_and_queue.stack import Node

class AnimalShelter:
    def __init__(self, front=None):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.front is None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = self.rear.next

    def dequeue(self, pref):
        if self.isEmpty():
            print("Queue is empty")
        else:
            if self.front.value == pref:
                deq_node = self.front
                self.front = self.front.next
                return deq_node
            else:

                while self.front.value != pref:
                    # I need to grab items from the front and enqueue them back.
                    item_value = self.front.value
                    self.enqueue(item_value)
                    self.front = self.front.next
            self.front = self.front.next
                #print("value not found")

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
    que1 = AnimalShelter()
    que1.enqueue("cat")
    que1.enqueue("dog")
    que1.enqueue("dog")
    que1.enqueue("cat")
    que1.enqueue("dog")

    print(str(que1.rear.value))
    print(str(que1.front.value))

    que1.dequeue("dog")
    que1.dequeue("dog")
    que1.dequeue("dog")
    que1.dequeue("dog")
    # que1.dequeue("dog")
    # que1.dequeue("dog")
    # print(str(que1.rear.value))
    # print(str(que1.front.value))

    print(que1.peek())
    print(que1.__str__())
