"""
DFS is a traversal algorithm that explores as far as possible along each branch before backtracking.
It can be implemented using both adjacency matrix and adjacency list.
"""

# Adjacent Matrix implementation
graph_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

def dfs_matrix(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in range(len(graph[start])):
        if graph[start][next] and next not in visited:
            dfs_matrix(graph, next, visited)
    return visited

print(dfs_matrix(graph_matrix, 0))


# Adjacent list implementation
graph_list = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

def dfs_list(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start]:
        if next not in visited:
            dfs_list(graph, next, visited)
    return visited

print(dfs_list(graph_list, 0))