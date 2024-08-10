from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sums = []
        queue = [root]

        while len(queue):
            level_nums = []

            for _ in range(len(queue)):
                curr = queue.pop()

                if curr.left:
                    queue.insert(0, curr.left)

                if curr.right:
                    queue.insert(0, curr.right)

                level_nums.append(curr.val)

            level_sums.append(sum(level_nums))

        max = level_sums[0]
        max_level = 1

        for i in range(1, len(level_sums)):
            if level_sums[i] > max:
                max = level_sums[i]
                max_level = i + 1

        return max_level
