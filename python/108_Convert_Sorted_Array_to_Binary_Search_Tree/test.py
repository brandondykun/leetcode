from solution import TreeNode, Solution, Optional
from collections import deque


class TestHelper(Solution):
    def tree_to_list_level_order(self, root: TreeNode) -> list[int]:
        """Level-Order Traversal: Layer by layer from top to bottom"""
        if not root:
            return []

        result = []
        queue = deque([root])

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

    # Helper to validate height-balanced BST property directly,
    # since multiple tree structures can be valid for the same array.
    def is_valid_balanced_bst(self, root: Optional[TreeNode]) -> bool:
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


sol = TestHelper()


#### Example 1:
nums = [-10, -3, 0, 5, 9]
answer_1 = [0, -3, 9, -10, None, 5]
answer_2 = [0, -10, 5, None, -3, None, 9]
output = sol.sortedArrayToBST(nums)
output_list = sol.tree_to_list_level_order(output)
valid = sol.is_valid_balanced_bst(output)
print(output_list == answer_1 or output_list == answer_2 and valid)

#### Example 2:
nums = [1, 3]
answer_1 = [3, 1]
answer_2 = [1, None, 3]
output = sol.sortedArrayToBST(nums)
output_list = sol.tree_to_list_level_order(output)
valid = sol.is_valid_balanced_bst(output)
print(output_list == answer_1 or output_list == answer_2 and valid)

#### Example 3 (extra):
nums = [0]
answer_1 = [0]
answer_2 = [0]
output = sol.sortedArrayToBST(nums)
output_list = sol.tree_to_list_level_order(output)
valid = sol.is_valid_balanced_bst(output)
print(output_list == answer_1 or output_list == answer_2 and valid)

#### Example 4 (extra):
nums = [-5, -2, 0, 3, 7]
answer_1 = [0, -5, 3, None, -2, None, 7]
answer_2 = [0, -2, 7, -5, None, 3]
output = sol.sortedArrayToBST(nums)
output_list = sol.tree_to_list_level_order(output)
valid = sol.is_valid_balanced_bst(output)
print(output_list == answer_1 or output_list == answer_2 and valid)

#### Example 5 (extra):
nums = [1, 2, 3, 4]
answer_1 = [2, 1, 3, None, None, None, 4]
answer_2 = [3, 1, 4, None, 2]
output = sol.sortedArrayToBST(nums)
output_list = sol.tree_to_list_level_order(output)
valid = sol.is_valid_balanced_bst(output)
print(output_list == answer_1 or output_list == answer_2 and valid)

#### Example 6 (extra):
nums = [-10000, -5000, 0, 5000, 10000]
answer_1 = [0, -10000, 5000, None, -5000, None, 10000]
answer_2 = [0, -5000, 10000, -10000, None, 5000]
output = sol.sortedArrayToBST(nums)
output_list = sol.tree_to_list_level_order(output)
valid = sol.is_valid_balanced_bst(output)
print(output_list == answer_1 or output_list == answer_2 and valid)

#### Example 7 (extra):
nums = [1, 2, 3, 4, 5, 6, 7]
answer_1 = [4, 2, 6, 1, 3, 5, 7]
answer_2 = [4, 2, 6, 1, 3, 5, 7]
output = sol.sortedArrayToBST(nums)
output_list = sol.tree_to_list_level_order(output)
valid = sol.is_valid_balanced_bst(output)
print(output_list == answer_1 or output_list == answer_2 and valid)
