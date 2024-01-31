"""
Implement a function that prints all paths that exist between two nodes (source to destination).
"""

# DFS solution
def print_all_paths(graph, source, destination):
    """
    Print all paths between source and destination
    :param graph: The graph
    :param source: Source vertex
    :param destination: Destination vertex
    :return: None
    """

    paths  = []
    visited = [False] * len(graph.graph)

    def dfs(current, path):
        visited[current] = True
        path.append(current)

        if current == destination:
            paths.append(path[:])
        else:
            temp = graph.graph[current]
            while temp:
                if not visited[temp.vertex]:
                    dfs(temp.vertex, path)
                temp = temp.next

        path.pop()
        visited[current] = False

    dfs(source, [])
    return paths

# Main to test the above program
if __name__ == "__main__":
    from graph import Graph
    V = 6
    g = Graph(V)
    g.add_edge(0, 2)
    g.add_edge(2, 5)
    g.add_edge(0, 1)
    g.add_edge(1, 4)
    g.add_edge(1, 3)
    g.add_edge(3, 5)
    g.add_edge(4, 5)

    print(g.print_graph())
    print(print_all_paths(g, 0, 5))