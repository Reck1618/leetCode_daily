"""
Implement BFS.
-> The breadth-first search (BFS) algorithm is used to search a tree or graph data structure for a node that meets a set of criteria.
   It starts at the tree's root or graph and searches/visits all nodes at the current depth level before moving on to the nodes at the next depth level.
    - we are doing traversal, and not searching for a target number.

Time -
Space -
"""

from collections import deque


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# Iterative
def bfs(root, result = []):
    if root is None:
        return result

    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result



# Driver code
root = Node(5)
root.left = Node(4)
root.right = Node(10)
root.left.left = Node(2)
root.left.right = Node(3)

print(bfs(root))