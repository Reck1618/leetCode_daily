"""
Implement a function that takes an undirected graph and prints all the connected components of a graph.
"""

import copy


def connected_components(graph):
    """
    Function to find the connected components
    :param graph: The graph
    :return: returns a list of connected components
    """

    # Write your code here!
    res = []
    visited = [False] * len(graph.graph)
    for i in range(len(graph.graph)):
        if not visited[i]:
            result = dfs(graph, i, visited)
            res.append(result)
    return res


# Helper Function of DFS. Might be useful
def dfs(g, source, visited):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return: returns the traversal in a list
    """

    graph = copy.deepcopy(g)

    # Create a stack for DFS
    stack = []

    # Result list
    result = []

    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack[-1]
        stack.pop()

        if not visited[source]:
            result.append(source)
            visited[source] = True

        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            graph.graph[source] = graph.graph[source].next

    return result


# Main program to test above function
if __name__ == "__main__":
    from graph import Graph
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    g.add_edge(5, 6)

    result = connected_components(g)

    print("Following are connected components")
    print(result)