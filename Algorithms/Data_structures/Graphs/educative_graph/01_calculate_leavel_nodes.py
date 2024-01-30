"""
Implement a function that returns the number of nodes at a given level starting from a root node of a directed graph.
"""

from collections import deque

# First solution
def number_of_nodes(graph, level):
    """
    Calculates the number of nodes at given level
    :param graph: The graph
    :return: Total number of nodes at given level
    """

    # Write your code here!
    source = 0
    visited = [0] * len(graph.graph)
    queue = deque([source])
    visited[source] = 1

    while queue:
        current = queue.popleft()

        temp = graph.graph[current]

        while temp is not None:
            data = temp.vertex
            if visited[data] == 0:
                queue.append(data)
                visited[data] = visited[current] + 1
            temp = temp.next


    count = 0
    for i in range(len(graph.graph)):
        if visited[i] == level:
            count += 1
    return count



# Second solution
def number_of_nodes(graph, level):
    """
    Calculates the number of nodes at given level
    :param graph: The graph
    :return: Total number of nodes at given level
    """

    # Write your code here!
    if level <= 1:
        return 1

    visited = [False] * len(graph.graph)
    queue = deque([0])
    visited[0] = True

    for current_level in range(1, level):
        nodes_at_current_level = len(queue)

        for _ in range(nodes_at_current_level):
            current = queue.popleft()
            temp = graph.graph[current]

            while temp is not None:
                data = temp.vertex
                if not visited[data]:
                    queue.append(data)
                    visited[data] = True
                temp = temp.next

    return len(queue)

