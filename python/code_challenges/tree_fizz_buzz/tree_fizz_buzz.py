class Node():
    def __init__(self, value):
        self.value = value
        self.children = []



class K_AryTree():
    def __init__(self, root=None):
        self.root = root

    def fizz_buzz_tree(tree):
        output = K_AryTree()

        def walk(root):


            if root.value % 3 == 0 and root.value % 5 == 0:
                node =  Node("FizzBuzz")
            elif root.value % 3 == 0:
                node = Node("Fizz")
            elif root.value % 5 == 0:
                node = Node("Buzz")
            else:
                node = Node(str(root.value))


            node.children = [walk(  child) for child in root.children]

            return node

        if tree.root is not None:
            output.root = walk(tree.root)

        return output
