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
            if(self.head is None):
                self.head = newNode
                return
            elif (self.head.value == value):
                # if the value is of the head node then call the insert method which adds elements to the beginnig of the linked list
                 self.insert(newNode.value)
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
                if not value:
                    return ("Error: the node with specified value is not in the linked list")
                current = self.head
                newNode = Node(newValue)
                while (current):
                    if(current.value == value):
                        newNode.next = current.next
                        current.next = newNode
                        return
                    current = current.next


    '''
        A method the find that accepts an integer that represenst an index of a node
        in a linked list. The method returns the value of that node starting counting
        from the backend. Eg, zero represents the last item in the linked list.
    '''
    def find_kth_value(self, k):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next

        current = self.head
        if (k > counter or k < 0):

            return ("Invalid input")
        else:
            for i in range(1, counter-k):

                current = current.next
            return current.value


    def zip_lists(self, ll1, ll2):
        #Set current for each ll to it's head
        ll3 = LinkedList()
        current_ll1 = ll1.head
        current_ll2 = ll2.head
        while current_ll1 or current_ll2:

            if current_ll1:
                ll3.append(current_ll1.value)
                current_ll1 = current_ll1.next

            if current_ll2:
                ll3.append(current_ll2.value)
                current_ll2 = current_ll2.next
        return ll3
        # # traverse through each linked list as long as neither has a value of None
        # while current_ll1 != None and current_ll2 != None:
        #     # Save the current next values of each list
        #     next_ll1 = current_ll1.next
        #     next_ll2 = current_ll2.next

        #     #swap the ll2 next to the next of next f ll1 while setting the next of ll1 to the current value of ll2
        #     current_ll2.next = next_ll1
        #     current_ll1.next = current_ll2

        #     # Adjust current for the next loop

        #     current_ll1 = next_ll1
        #     current_ll2 = next_ll2
        #     ll2.head = current_ll2


ll1 = LinkedList()
ll1.insert(1)
ll1.insert(3)
ll1.insert(2)
ll1.insert(6)
ll1.insert(7)
ll2 = LinkedList()
ll2.insert(5)
ll2.insert(9)
ll2.insert(4)
ll3 = LinkedList()
print(ll3.zip_lists(ll1, ll2))
#print(ll1.__str__())
