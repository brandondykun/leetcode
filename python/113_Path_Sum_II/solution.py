from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node: Optional[TreeNode], sum: int, curr_path: List):
            if not node:
                return

            curr_path.append(node.val)

            if sum == node.val and not node.right and not node.left:
                result.append(list(curr_path))

            else:
                dfs(node.left, sum - node.val, curr_path)
                dfs(node.right, sum - node.val, curr_path)

            curr_path.pop()

        dfs(root, targetSum, [])
        return result
