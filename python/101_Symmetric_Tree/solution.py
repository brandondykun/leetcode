from typing import Optional
from collections import deque

from leetcode_utils.binary_tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([(root.left, root.right)])

        while queue:
            left_node, right_node = queue.popleft()

            if not left_node and not right_node:
                continue

            if not left_node or not right_node or left_node.val != right_node.val:
                return False

            queue.append((left_node.left, right_node.right))
            queue.append((left_node.right, right_node.left))

        return True
