class Graph:
    def __init__(self):
        self.adjacency_list = {}
        # key will be the node, value adj node with a value of the edge

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex
        # Arguments: value
        # Returns: The added node
        # Add a node to the graph or add to adj list

    def add_edge(self, vertex_a, vertex_z, weight=1):
        if vertex_a not in self.adjacency_list:
            print("Value doesn't exist")

            edge = Edge(vertex_z, weight)
            self.adjacency_list[vertex_a].append(edge)

        # Arguments: 2 nodes to be connected by the edge, weight (optional)
        # Returns: nothing
        # Adds a new edge between two nodes in the graph
        # If specified, assign a weight to the edge
        # Both nodes should already be in the Graph

    def get_nodes(self):
        all_nodes = list(self.adjacency_list.keys())
        return all_nodes

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]
        # Arguments: node
        # Returns a collection of edges connected to the given node
        # Include the weight of connection in returned collection

    def size(self):
        size = len(self.adjacency_list)
        return size


class Vertex:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return(self.value)


class Edge:
    def __init__(self, vertex, weight=1):
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
