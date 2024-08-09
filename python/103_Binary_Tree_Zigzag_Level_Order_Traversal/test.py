from typing import Optional
from solution import TreeNode, Solution


class TestHelper(Solution):
    def build_tree(self, arr: list[int | None]) -> TreeNode | None:
        """Build a binary tree from a list."""
        if len(arr) == 0:
            return None

        nodes = []

        val = arr.pop(0)
        root = TreeNode(val)
        nodes.append(root)

        while len(arr) > 0:
            curr = nodes.pop(0)

            left_val = arr.pop(0)
            if left_val is not None:
                curr.left = TreeNode(left_val)
                nodes.append(curr.left)

            if len(arr) > 0:
                right_val = arr.pop(0)
                if right_val is not None:
                    curr.right = TreeNode(right_val)
                    nodes.append(curr.right)

        return root


sol = TestHelper()

print("Tests - 103. Binary Tree Zigzag Level Order Traversal: ")


def test_runner(input: list[int], expected: list[list[int]]):
    """Helper function to test different inputs/outputs.
    Convert input list to binary tree, call zigzagLevelOrder
    and compare the output to the expected list.
    """
    root_node = sol.build_tree(input)
    output = sol.zigzagLevelOrder(root_node)
    print(output == expected)


### Example 1:
input = [3, 9, 20, None, None, 15, 7]
expected = [[3], [20, 9], [15, 7]]
test_runner(input, expected)

### Example 2:
input = [1]
expected = [[1]]
test_runner(input, expected)

### Example 3:
input = []
expected = []
test_runner(input, expected)

### Example 4 (extra):
input = [1, 2, 3, 4, 5, 6, 7, None, None, 8, 9]
expected = [[1], [3, 2], [4, 5, 6, 7], [9, 8]]
test_runner(input, expected)

### Example 5 (extra):
input = [1, 2]
expected = [[1], [2]]
test_runner(input, expected)
