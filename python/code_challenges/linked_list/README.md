# Singly Linked List
<!-- Short summary or background information -->
C
## Challenge
<!-- Description of the challenge -->
Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Linked List
Create a Linked List class
Within your Linked List class, include a head property.
Upon instantiation, an empty Linked List should be created.
The class should contain the following methods
insert
Arguments: value
Returns: nothing
Adds a new node with that value to the head of the list with an O(1) Time performance.
includes
Arguments: value
Returns: Boolean
Indicates whether that value exists as a Node’s value somewhere within the list.
to string
Arguments: none
Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O
time O(n) as every node is visited once.
space O(n)

#
<!-- Description of each method publicly available to your Linked List -->
 an insert a method to insert a node into the linked list.
 the method receives a value and uses it to add a new node. then checks whether there is head. If no head then it sets the head to the new node<br/>

 includes method that receives a value and traverses the linked list to find the value. If value is found, it returns true, otherwise it returns false.<br/>

 a to_string method that traverses the linked list and returns a string representation of the linked list.

