"""
Implement a Binary tree.
"""
#  Create a node
from collections import deque

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Print the tree (inorder traversal)
    def print_tree(self):
        return self._print_tree(self.root)

    def _print_tree(self, root, result = None):
        if result is None:
            result = []

        if root:
            self._print_tree(root.left, result)
            result.append(root.val)
            self._print_tree(root.right, result)
        return result


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


    # Delete a node in the tree
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            # if the node has one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: get the inorder successor
            root.val = self._min_value_node(root.right).val
            root.right = self._delete(root.right, root.val)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


    # Search for a node in the tree
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root is not None

        if root.val < key:
            return self._search(root.right, key)
        else:
            return self._search(root.left, key)


    # Bredth-First search
    def bfs(self):
        return self._bfs(self.root)

    def _bfs(self, root):
        result = []

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


    # Find the height of the tree
    def height(self):
        return self._height(self.root)

    def _height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self._height(root.left), self._height(root.right))


    # Find the minimum value in the tree
    def min_value(self):
        return self._min_value(self.root)

    def _min_value(self, root):
        current = root
        while current.left:
            current = current.left
        return current.val


    # Find the maximum value in the tree
    def max_value(self):
        return self._max_value(self.root)

    def _max_value(self, root):
        current = root
        while current.right:
            current = current.right
        return current.val


    # Check if the tree is a binary search tree
    def is_bst(self):
        return self._is_bst(self.root, float('-inf'), float('inf'))

    def _is_bst(self, root, min_val, max_val):
        if root is None:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self._is_bst(root.left, min_val, root.val) and self._is_bst(root.right, root.val, max_val)


    # Check if the tree is balanced
    def is_balanced(self):
        return self._is_balanced(self.root)[0]

    def _is_balanced(self, root):
        if root is None:
            return True, 0

        left_balanced, left_height = self._is_balanced(root.left)
        right_balanced, right_height = self._is_balanced(root.right)

        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return balanced, 1 + max(left_height, right_height)


    # Find the lowest common ancestor of two nodes in bst
    def lca(self, node1, node2):
        return self._lca(self.root, node1, node2)

    def _lca(self, root, node1, node2):
        if root is None:
            return None
        if root.val > node1 and root.val > node2:
            return self._lca(root.left, node1, node2)
        if root.val < node1 and root.val < node2:
            return self._lca(root.right, node1, node2)
        return root.val


# Driver code
tree = BinarySearchTree()
tree.insert(50)
tree.insert(30)
tree.insert(60)
tree.insert(10)
tree.insert(40)
tree.insert(29)
tree.delete(30)
print(tree.is_balanced())
