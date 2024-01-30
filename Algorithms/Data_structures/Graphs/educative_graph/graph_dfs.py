"""
Graph Traversal (DFS) implementation on educative.com
"""

def dfs(graph, source):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """

    # Write your code here!
    visited = [False] * (len(graph.graph))

    result = []
    stack = []

    stack.append(source)

    while stack:

        current = stack.pop()

        if not visited[current]:
            result.append(current)
            visited[current] = True

        while graph.graph[current] is not None:
            data = graph.graph[current].vertex
            if not visited[data]:
                stack.append(data)
            graph.graph[current] = graph.graph[current].next

    return "".join(map(str, result))



# Main to test the above program
if __name__ == "__main__":
    from graph import Graph
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(dfs(g, 0))