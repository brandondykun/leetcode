from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def build_nums(node: Optional[TreeNode]) -> List[str]:
            if not node.right and not node.left:
                return [str(node.val)]

            left_tree = []
            right_tree = []

            if node.right:
                right_tree = build_nums(node.right)

            if node.left:
                left_tree = build_nums(node.left)

            return [str(node.val) + num for num in left_tree + right_tree]

        str_nums = build_nums(root)
        sum = 0

        for num in str_nums:
            sum += int(num)

        return sum
