"""
BFS is a traversal algorithm that explores all the vertices at the current depth before moving on to the vertices at the next depth.
"""
from collections import deque

# Adjacent Matrix implementation
graph_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

def bfs_matrix(graph, start):
    result = []
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        result.append(current)

        for next in range(len(graph)):
            if graph[current][next] and not visited[next]:
                queue.append(next)
                visited[next] = True
    return result

print(bfs_matrix(graph_matrix, 0))


# Adjacent List implementation
graph_list = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

def bfs_list(graph, start):
    result = []
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        result.append(current)

        for next in graph[current]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
    return result

print(bfs_list(graph_list, 0))