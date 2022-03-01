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
                output.children.append(node)
            elif root.value % 3 == 0:
                node = Node("Fizz")
                output.children.append(node)
            elif root.value % 5 == 0:
                node = Node("Buzz")
                output.children.append(node)
            else:
                node = Node(str(root.value))

            return node

        if tree.root is not None:
            output.root = walk(tree.root)

        return output
