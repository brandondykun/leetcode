from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if root.val == targetSum and not root.right and not root.left:
            return True

        val = targetSum - root.val

        return self.hasPathSum(root.left, val) or self.hasPathSum(root.right, val)
