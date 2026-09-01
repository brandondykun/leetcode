from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Recursively prune left and right subtrees
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # If the current node is 0 and has no remaining children, prune it
        if root.val == 0 and not root.left and not root.right:
            return None

        return root
