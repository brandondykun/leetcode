from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return [f"{root.val}"]

        left = []
        right = []

        if root.left:
            left_traversal = self.binaryTreePaths(root.left)

            for path in left_traversal:
                left.append(f"{root.val}->{path}")

        if root.right:
            right_traversal = self.binaryTreePaths(root.right)

            for path in right_traversal:
                right.append(f"{root.val}->{path}")

        return left + right
