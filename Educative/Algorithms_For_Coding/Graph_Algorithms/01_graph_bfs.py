"""
Graph Traversal (BFS) implementation on educative.com
"""

from collections import deque

def bfs(graph, source):
    """
    Function to print a BFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """

    # Write your code here!
    visited = [False] * (len(graph.graph))

    result = []
    queue = deque([source])

    visited[source] = True

    while queue:
        current = queue.popleft()
        result.append(current)

        temp = graph.graph[current]

        while temp is not None:
            data = temp.vertex

            if not visited[data]:
                queue.append(data)
                visited[data] = True
            temp = temp.next

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

    print(bfs(g, 0))