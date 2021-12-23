class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # a method to insert a node into the list
    def insert(self, value):
        newNode = Node(value)
        if(self.head is not None):
            # if we have head then we set the current node to head
            newNode.next = self.head
        self.head = newNode


    # a method to search the linked list to see if it includes a specific value
    def includes(self, value):
        current = self.head
        while(current):
            if current.value == value:
                return True
            current = current.next

        return False


    # method to return a string representation for the linked list nodes
    def __str__(self):
        if self.head is None:
            print("Empty linked list")
            return

        current = self.head
        nodes = " "

        while(current):
            nodes += (f'{{ {current.value} }} -> ')
            current = current.next
        nodes = (f'{nodes}NULL')
        return nodes

    '''
    a method to append a node with a given value at the end of the linked list
    If the linked list is empty set the new node to be the head
    else traverse the list as long as there is a next node
    at the end of the list append the new node
    '''
    def append(self, value):
        newNode = Node(value)
        if(self.head is None):
            self.head = newNode
            return
        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode

    '''
    a method to insert a node with a given value before another node of the linked list
    If the linked list is empty set the new node to be the head, if the value doesn't exist return an error.
    else traverse the list as until you find the specified value then insert the new node before it.
    '''
    def insert_before(self, value, newValue):
            current = self.head
            newNode = Node(newValue)
            previous = None
            if(self.head is None):
                self.head = newNode
                return
            elif (current.value == value):
                newNode.next = current
                current.next = newNode
            else:
                while (current.next):
                    if(current.next.value == value):

                        newNode.next = current.next
                        current.next = newNode
                        return
                    current = current.next

                return ("Error: the node with specified value is not in the linked list")
    '''
    a method to insert a node with a given value after another specific node's value of the linked list
    If the linked list is empty set the new node to be the head, if the value doesn't exist return an error.
    else traverse the list until you find the specified value then insert the new node after it.
    '''
    def insert_after(self, value, newValue):
                current = self.head
                while (current):
                    if(current.value == value):
                        newNode = Node(newValue)
                        newNode.next = current.next.next
                        current.next = newNode
                        return
                    current = current.next
                return ("Error: the node with specified value is not in the linked list")

linked_list = LinkedList()
linked_list.insert('1')
linked_list.insert('2')
linked_list.insert('3')
linked_list.includes('4')
linked_list.append('5')
linked_list.insert_before('5','6')
linked_list.insert_after(2, 11)

print(linked_list.__str__())
