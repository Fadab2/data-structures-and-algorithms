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
        nodes = " "
        current = self.head
        while(current):
            #print(f'{current.value}->')
            nodes = current.value
            print( "{ "+nodes+ " }" + "-> ", end="")
            current = current.next
        #return  print(f'{nodes}-> NULL')
        print("NULL")

    '''
    a method to append a node with a given value at the end of the linked list
    If the linked list is empty set the new node to be the head
    else traverse the list as long as there is a next node
    at the end of the list append the new node
    '''
    def append(self, value):
        newNode = Node(value)
        if(self.head is not None):
            self.head = newNode
            return
        current = self.head
        while (current.next is not None):
            current = current.next
            current.next = newNode





linked_list = LinkedList()
linked_list.insert('a')
linked_list.insert('b')
linked_list.insert('c')
linked_list.includes('a')
linked_list.append('d')


linked_list.__str__()
