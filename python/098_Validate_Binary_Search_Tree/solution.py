from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs_validation(
            node: Optional[TreeNode],
            min_node: Optional[TreeNode],
            max_node: Optional[TreeNode],
        ) -> bool:
            if not node:
                return True
            if min_node and node.val <= min_node.val:
                return False
            if max_node and node.val >= max_node.val:
                return False

            return dfs_validation(node.left, min_node, node) and dfs_validation(
                node.right, node, max_node
            )

        return dfs_validation(root, None, None)
