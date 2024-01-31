"""
You have to implement a function which will take a graph as input and print its transpose.
"""

# Solution
def transpose_graph(graph):
    """
    Transpose the given graph
    :param graph: The graph
    :return: Transposed graph
    """

    transpose = Graph(len(graph.graph))
    for source in range(len(graph.graph)):
        temp = graph.graph[source]
        while temp is not None:
            destination = temp.vertex
            transpose.add_edge(destination, source)
            temp = temp.next
    return transpose


# Main to test the above program
if __name__ == "__main__":
    from graph import Graph
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(g.print_graph())
    print(transpose_graph(g).print_graph())
