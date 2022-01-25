# Challenge Summary
<!-- Description of the challenge -->
Feature Tasks
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue.
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
The class should contain the following methods:
* push, pop, peek, is empty

reate a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
The class should contain the following methods:
* enqueue, dequeue, peek, is empty


## Whiteboard Process
<!-- Embedded whiteboard image -->


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Created a Node class which takes the value of the node and the next node.
Created Stack class that takes the top node with a default value of None.
Created a Queue class that takes front and rear nodes with a default value of None.
Using Test-driven development implemented all the above methods one by one until all test passed.

Big O
time: O(1) all methods have time complexity of O(1) regardless of the number of nodes.
space: O(1) all methods have space complexity of O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->
* The solution used test-driven development and all the below test passed.
* Can successfully push onto a stack
* Can successfully push multiple values onto a stack
* Can successfully pop off the stack
* Can successfully empty a stack after multiple pops
* Can successfully peek the next item on the stack
* Can successfully instantiate an empty stack
* Calling pop or peek on empty stack raises exception
* Can successfully enqueue into a queue
* Can successfully enqueue multiple values into a queue
* Can successfully dequeue out of a queue the expected value
* Can successfully peek into a queue, seeing the expected value
* Can successfully empty a queue after multiple dequeues
* Can successfully instantiate an empty queue
* Calling dequeue or peek on empty queue raises exception

