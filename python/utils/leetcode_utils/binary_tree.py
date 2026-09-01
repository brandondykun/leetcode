from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeUtil:
    @staticmethod
    def build_tree(arr: list[int | None]) -> TreeNode | None:
        if not arr:
            return None

        root_val = arr[0]
        if root_val is None:
            return None

        root = TreeNode(root_val)
        queue = deque([root])
        index = 1  # Use a pointer instead of arr.pop(0)

        while queue and index < len(arr):
            curr = queue.popleft()

            # Left Child
            if index < len(arr):
                left_val = arr[index]
                if left_val is not None:
                    left_node = TreeNode(left_val)
                    curr.left = left_node
                    queue.append(left_node)
                index += 1

            # Right Child
            if index < len(arr):
                right_val = arr[index]
                if right_val is not None:
                    right_node = TreeNode(right_val)
                    curr.right = right_node
                    queue.append(right_node)
                index += 1

        return root

    @staticmethod
    def tree_to_list_level_order(root: TreeNode) -> list[int]:
        """Level-Order Traversal: Layer by layer from top to bottom"""
        if not root:
            return []

        result = []
        queue: deque[TreeNode | None] = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Trim trailing None values from the list
        while result and result[-1] is None:
            result.pop()

        return result

    @staticmethod
    def is_valid_balanced_bst(root: Optional[TreeNode]) -> bool:
        """
        Helper to validate height-balanced BST property directly,
        since multiple tree structures can be valid for the same array.
        """

        # Define min_val and max_val explicitly as positional parameters
        def check(node, min_val, max_val):
            if not node:
                return True, 0, float("inf"), float("-inf")

            # 1. Validate BST bounds
            if not (min_val < node.val < max_val):
                return False, 0, 0, 0

            # 2. Recurse passing positional arguments
            left_valid, left_h, left_min, left_max = check(node.left, min_val, node.val)
            right_valid, right_h, right_min, right_max = check(
                node.right, node.val, max_val
            )

            # 3. Validate height balance
            is_balanced = abs(left_h - right_h) <= 1

            total_valid = left_valid and right_valid and is_balanced
            height = max(left_h, right_h) + 1
            min_node_val = min(node.val, left_min)
            max_node_val = max(node.val, right_max)

            return total_valid, height, min_node_val, max_node_val

        # Pass initial bounds to the root call
        valid, _, _, _ = check(root, float("-inf"), float("inf"))
        return valid
