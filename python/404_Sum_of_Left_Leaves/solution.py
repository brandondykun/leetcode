from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS Solution
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total_sum = 0

        queue = deque([(root, False)])

        while queue:
            node, is_left_node = queue.popleft()

            if is_left_node and not node.left and not node.right:
                total_sum += node.val

            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))

        return total_sum


# Recursive DFS Solution
# class Solution:
#     def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
#         def dfs(node: Optional[TreeNode], is_left: bool) -> int:
#             if not node:
#                 return 0

#             # Base case: if it's a leaf node
#             if not node.left and not node.right:
#                 return node.val if is_left else 0

#             # Recurse on left and right subtrees
#             return dfs(node.left, True) + dfs(node.right, False)

#         return dfs(root, False)
