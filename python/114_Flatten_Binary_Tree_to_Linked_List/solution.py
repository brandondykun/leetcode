from typing import Optional
from collections import deque

from leetcode_utils.binary_tree import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        queue = deque([])

        def dfs(node: TreeNode | None):
            if not node:
                return None

            queue.append(node)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        curr = queue.popleft()

        while queue:
            next = queue.popleft()
            curr.left = None
            curr.right = next
            curr = next
