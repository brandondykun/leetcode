from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        val = targetSum - root.val

        if val == 0 and not root.left and not root.right:
            return [[root.val]]

        left_child = []
        right_child = []

        if root.left:
            left = self.pathSum(root.left, val)
            for item in left:
                if len(item):
                    item.insert(0, root.val)
            left_child = left
        if root.right:
            right = self.pathSum(root.right, val)
            for item in right:
                if len(item):
                    item.insert(0, root.val)
            right_child = right

        output = []

        if len(left_child):
            output += left_child

        if len(right_child):
            output += right_child

        return output
