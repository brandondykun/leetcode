from typing import Optional

from leetcode_utils.binary_tree import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root

        next_node = root.left if val < root.val else root.right
        return self.searchBST(next_node, val)
