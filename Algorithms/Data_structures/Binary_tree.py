"""
Implement a Binary tree.
"""

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None


    # Insert a node in the tree
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.val:
                root.left = self._insert(root.left, key)
            else:
                root.right = self._insert(root.right, key)

        return root

    # Print the tree (inorder traversal)
    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, root):
        if root:
            self._print_tree(root.left)
            print(root.val)
            self._print_tree(root.right)




# Driver code
tree = BinarySearchTree()
tree.insert(50)
tree.insert(30)
tree.insert(60)
tree.print_tree()
