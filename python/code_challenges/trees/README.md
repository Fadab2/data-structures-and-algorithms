# Trees
<!-- Short summary or background information -->
To create a binary tree with the 3 traversals, pre-order, in-order and post-order. Add a binary search tree class to add values to the search binary tree and contains method to check for a passed value in the binary tree.

## Challenge
<!-- Description of the challenge -->
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
Binary Tree

Create a Binary Tree class

Define a method for each of the depth first traversals:

pre order
in order

post order which returns an array of the values, ordered appropriately.

Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

Binary Search Tree

Create a Binary Search Tree class

This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:

Add:

Arguments: value

Return: nothing

Adds a new node with that value in the correct location in the binary search tree.

Contains:

Argument: value

Returns: boolean indicating whether or not the value is in the tree at least once.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

declare a node class with value, left and right.
declare a binary tree class with root node.
define pre-order method which traverses root->left->right
define in-order method that traverses left->root->right
define a post-order method that traverses left->right->root
declare a search binary tree class that extends binary tree class.

define an add method that adds element to the tree:
check the root is none. if so assign the new node to root.
if root.value < value:
check to the right
if root.value > value:
and there is a left node
then check to the left of the root.
else assign the value to the root.

## API
<!-- Description of each method publicly available in each of your trees -->




