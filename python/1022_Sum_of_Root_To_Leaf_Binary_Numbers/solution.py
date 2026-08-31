from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        output = []

        def dfs(node: Optional[TreeNode], curr_num: List[str]):
            if not node:
                return

            curr = curr_num + [str(node.val)]

            if not node.right and not node.left:
                return output.append(curr)
            else:
                dfs(node.left, curr)
                dfs(node.right, curr)

            curr.pop()

        dfs(root, [])

        return sum([int("".join(x), 2) for x in output])
