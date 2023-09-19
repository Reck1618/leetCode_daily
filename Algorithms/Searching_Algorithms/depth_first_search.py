"""
Implement DFS.
-> Depth-first search (DFS) is a method for exploring a tree or graph. In a DFS, you go as deep as possible down one path before backing up and trying a different one.
    - we are doing traversal, and not searching for a target number.

Time - O(n)
Space - O(n)
"""
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Inorder
def dfs(root, visited_nodes = None):
    if visited_nodes is None:
        visited_nodes = []

    if root:
        dfs(root.left, visited_nodes)
        visited_nodes.append(root.val)
        dfs(root.right, visited_nodes)

    return visited_nodes


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Traversal
print(dfs(root))