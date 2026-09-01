from typing import Optional

from leetcode_utils.binary_tree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        tmp = root.right
        root.right = root.left
        root.left = tmp

        return root
