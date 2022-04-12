from stack_and_queue.stack import Stack
from stack_and_queue.queue import Queue
from graph_breadth_first.graph_breadth_first import Graph


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, vertex_start, vertex_end, weight=0):
        if vertex_start not in self.adjacency_list:
            print("Value doesn't exist")

            edge = Edge(vertex_end, weight)
            self.adjacency_list[vertex_start].append(edge)

    def get_nodes(self):
        all_nodes = list(self.adjacency_list.keys())
        return all_nodes

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def size(self):
        size = len(self.adjacency_list)
        return size

    def bread_first(self, vertex):
        nodes = []
        breadth = Queue()
        visited = set()
        breadth.enqueue(vertex)
        visited.Add(vertex)

        while not breadth.isEmpty():
            front = breadth.dequeue()
            nodes.append(front.value)
            children = self.adjacency_list[front.value]

            for child in children:
                if front not in visited:
                    visited.add[front.value]
                    breadth.enqueue(child)

            return nodes

    def depth_first(self, root):
        stack = Stack()
        node = stack.push(root)
        visited = set()
        visited.add(root)
        while stack not in self.isEmpty():
             node = stack.peek()
             visited.add(node)
             stack.push(node)
             neighbors = self.get_neighbors(node)
             for child in neighbors:
                if child not in visited:
                    visited.add(node)
                    stack.push(node)

        return visited

class Vertex:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return(self.value)


class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

    def __repr__(self):
        return f'{self.vertex}, {self.weight}'


if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("G")
    graph.add_node("D")
    graph.add_node("E")
    print(graph.get_nodes())

    # graph.add_node("C")
    # graph.add_edge(A, B, 3)
    # print(graph.__repr__())
    # print(graph.get_neiggbors(B))
    # print(graph.size())
    # print(edge.__repr__())
