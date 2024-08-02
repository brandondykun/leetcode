from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output = []

        if not root:
            return output

        queue = [root]

        while len(queue) > 0:
            count = 0
            total = 0

            for _ in range(len(queue)):
                curr = queue.pop()
                count += 1
                total += curr.val

                if curr.left:
                    queue.insert(0, curr.left)

                if curr.right:
                    queue.insert(0, curr.right)

            output.append(total / count)

        return output
