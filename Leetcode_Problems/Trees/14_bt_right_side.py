"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
"""
import collections

class Solution:
    def rightSideView(self, root):
        result = []

        if root is None:
            return result

        queue = collections.deque([root])

        while queue:
            value = []

            for i in range(len(queue)):
                node = queue.popleft()
                value.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(value[-1])
        return result