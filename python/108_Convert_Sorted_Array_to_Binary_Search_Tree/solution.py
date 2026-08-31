from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(lst: List[int], start: int, end: int):
            if start > end:
                return None

            middle = (start + end) // 2
            node = TreeNode(val=lst[middle])

            node.left = buildTree(lst, start, middle - 1)
            node.right = buildTree(lst, middle + 1, end)

            return node

        return buildTree(nums, 0, len(nums) - 1)
