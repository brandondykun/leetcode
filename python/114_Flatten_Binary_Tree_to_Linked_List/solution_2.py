from typing import Optional

from leetcode_utils.binary_tree import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal prev
            if not node:
                return

            dfs(node.right)
            dfs(node.left)

            node.right = prev
            node.left = None
            prev = node

        dfs(root)
