
from code_challenges.trees.node import Node
from code_challenges.trees.binary_trees import BinaryTree
from code_challenges.trees.binary_search_tree import BinarySearchTree
from code_challenges.stack_and_queue.queue import Queue


def breadth_frist(root):
    breadth = Queue()
    return_list = []

    if breadth.front == None:
        return return_list

    breadth.enqueue(root)

    while breadth:
        front_node = breadth.dequeue()
        return_list.append(front_node.value)

        if root.left is not None:
            breadth.enqueue(root.left)

        if root.right is not None:
            breadth.enqueue(root.left)

    return return_list
