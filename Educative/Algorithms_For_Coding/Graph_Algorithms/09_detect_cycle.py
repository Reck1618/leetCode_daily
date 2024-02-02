"""
The concept of loops or cycles is very common in graph theory. A cycle exists when you traverse the graph and come upon a vertex which has already been visited.
You have to implement the detect_cycle function which tells you whether or not a graph contains a cycle.
"""

# Solution for both directed and undirected graphs
def detect_cycle(graph):
    """
    A function to detect a cycle in a graph
    :param graph: A graph
    :return: True if a cycle exists, False otherwise
    """
    visited = [False] * graph.V

    def detect_cycle_recursive(node):
        if visited[node]:
            return True

        visited[node] = True
        head = graph.graph[node]
        while head:
            if detect_cycle_recursive(head.vertex):
                return True
            head = head.next

        visited[node] = False
        return False


    for node in range(graph.V):
        if detect_cycle_recursive(node):
            return True

    return False


# Main program to test the above code
if __name__ == "__main__":
    from graph import Graph
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(3, 0)

    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    print(detect_cycle(g1))
    print(detect_cycle(g2))