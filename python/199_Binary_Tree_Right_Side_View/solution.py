from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        if not root:
            return output

        queue = [root]

        while len(queue) > 0:
            level_nodes = []

            for _ in range(len(queue)):
                curr = queue.pop()
                level_nodes.append(curr.val)

                if curr.left:
                    queue.insert(0, curr.left)

                if curr.right:
                    queue.insert(0, curr.right)

            output.append(level_nodes[-1])

        return output
