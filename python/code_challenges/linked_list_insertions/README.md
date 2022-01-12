# Challenge Summary
<!-- Description of the challenge -->
Feature Tasks
Write the following methods for the Linked List class:

append
arguments: new value
adds a new node with the given value to the end of the list
insert before
arguments: value, new value
adds a new node with the given new value immediately before the first node that has the value specified
insert after
arguments: value, new value
adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process
<!-- Embedded whiteboard image -->
![whiteboard](../linked_list_insertions/linked-list-insertions.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
We traversed the linked list and added the appended value to the end of the list by pointing the newnode to the last node and then pointing the previously last node (tail) to the newnode.

For inserting before the giving value, we checked the value we want to insert after is already exist, if not then display an exception and abort. if it exist then we traverse the linked list and once we find the value we
point the the newnode to the node with the intended value and point the node before the intended node to the newnode.

For inserting after the giving value, we checked the value we want to insert after is already exist, if not then display an exception and abort. if it exist then we traverse the linked list and once we find the value we
point the the newnode to the node that is next of the intended value and point the intended node to the newnode.

Big O
time: O(n) as every node is visited once.
space: O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->
