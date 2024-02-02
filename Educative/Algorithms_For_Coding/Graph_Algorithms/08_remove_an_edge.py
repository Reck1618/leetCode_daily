"""
You must implement the remove_edge function which takes a source and a destination as arguments.
If an edge exists between the two, it should be deleted. Print the breadth-first traversal on the resultant graph.
"""

def remove_edge(graph, source, destination):
    """
    A function to remove an edge
    :param graph: A graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """

    # Write your code here!
    if source < 0 or source >= graph.V or destination < 0 or destination >= graph.V:
        print("Invalid source or destination vertex.")
        return

    current = graph.graph[source]

    if not current:
        print("Edge does not exist. No removal needed.")
        return

    if current.vertex == destination:
        graph.graph[source] = current.next
        return

    while current.next:
        vertex = current.next.vertex
        if vertex == destination:
            current.next = current.next.next
            return
        current = current.next



# Main to test the above program
if __name__ == "__main__":
    from graph import Graph
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(g.bfs())
    remove_edge(g, 1, 3)
    print(g.bfs())
    remove_edge(g, 0, 1)
    print(g.bfs())