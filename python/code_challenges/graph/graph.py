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
    A = graph.add_node("A")
    B = graph.add_node("B")
    C = graph.add_node("C")
    D = graph.add_node("D")
    print(graph.get_nodes())
    nieghbor = graph.add_edge(A, B, 3)
    print(len(nieghbor))
    # graph.add_node("C")
    # graph.add_edge(A, B, 3)
    # print(graph.__repr__())
    # print(graph.get_neiggbors(B))
    # print(graph.size())
    # print(edge.__repr__())
