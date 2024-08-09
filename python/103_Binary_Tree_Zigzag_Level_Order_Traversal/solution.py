from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        if not root:
            return output

        queue = [root]
        level_count = 1

        while len(queue):
            level = []
            for _ in range(len(queue)):
                curr = queue.pop()

                if curr.left:
                    queue.insert(0, curr.left)

                if curr.right:
                    queue.insert(0, curr.right)

                if level_count % 2 != 0:
                    level.append(curr.val)
                else:
                    level.insert(0, curr.val)

            output.append(level)
            level_count += 1

        return output
