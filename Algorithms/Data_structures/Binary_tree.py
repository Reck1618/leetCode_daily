"""
Implement a Binary tree.
"""
#  Create a node
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

    def _print_tree(self, root, result = []):
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




# Driver code
tree = BinarySearchTree()
tree.insert(50)
tree.insert(30)
tree.insert(60)
tree.insert(10)
tree.insert(40)
tree.insert(25)
tree.insert(29)
tree.delete(30)
print(tree.print_tree())
