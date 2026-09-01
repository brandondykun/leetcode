from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if not left:
                node.left = None
            if not right:
                node.right = None

            return left + right + node.val

        total_sum = dfs(root)

        if not total_sum:
            return None

        return root
