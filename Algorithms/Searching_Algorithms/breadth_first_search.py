"""
Implement BFS.
-> The breadth-first search (BFS) algorithm is used to search a tree or graph data structure for a node that meets a set of criteria. 
   It starts at the tree's root or graph and searches/visits all nodes at the current depth level before moving on to the nodes at the next depth level.
    - we are doing traversal, and not searching for a target number.

Time -
Space -
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Iterative
def bfs(root):
    pass






# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)