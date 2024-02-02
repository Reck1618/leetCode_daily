from graph import Graph

def is_strongly_connected(graph):
    """
    Finds if the graph is strongly connected or not
    :param graph: The graph
    :return: returns True if the graph is strongly connected, otherwise False
    """

    # DFS function
    def dfs(graph, source):
        visited = [False] * len(graph.graph)
        result = []
        stack = []

        stack.append(source)

        while stack:
            current = stack.pop()

            if not visited[current]:
                result.append(current)
                visited[current] = True

            current_neighbor = graph.graph[current]
            while current_neighbor is not None:
                data = current_neighbor.vertex
                if not visited[data]:
                    stack.append(data)
                current_neighbor = current_neighbor.next

        return result

    # Transpose function
    def transpose(graph):
        transpose = Graph(len(graph.graph))

        for source in range(len(graph.graph)):
            current_neighbor = graph.graph[source]
            while current_neighbor is not None:
                destination = current_neighbor.vertex
                transpose.add_edge(destination, source)
                current_neighbor = current_neighbor.next
        return transpose


    result_1 = dfs(graph, 0)
    graph2 = transpose(graph)
    result_2 = dfs(graph2, 0)

    return len(result_1) == len(result_2)


# Main program to test the above code
if __name__ == "__main__":

    V = 5
    g1 = Graph(V)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(3, 0)
    g1.add_edge(4, 2)
    print("Yes" if is_strongly_connected(g1) else "No")

    g2 = Graph(V)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(2, 4)
    print ("Yes" if is_strongly_connected(g2) else "No")