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
    def to_string(self):
        nodes = " "
        current = self.head
        while(current):
            #print(f'{current.value}->')
            nodes = current.value
            print( "{ "+nodes+ " }" + "-> ")
            current = current.next
        #return  print(f'{nodes}-> NULL')
        print("NULL")


linked_list = LinkedList()
linked_list.insert('a')
linked_list.insert('b')
linked_list.insert('c')
linked_list.includes('a')

linked_list.to_string()
