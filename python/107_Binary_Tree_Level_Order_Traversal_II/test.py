from solution import TreeNode, Solution


class TestHelper(Solution):
    def build_tree(self, arr: list[int | None]) -> TreeNode | None:
        """Build a binary tree from a list."""
        if len(arr) == 0:
            return None

        nodes: list[TreeNode] = []

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

print("Tests - 107. Binary Tree Level Order Traversal II: ")


def test_runner(input: list[int | None], expected: list[list[int]]):
    """Helper function to test different inputs/outputs.
    Convert input list to binary tree, calls levelOrderBottom
    method, compares output to expected output list.
    """
    root_node = sol.build_tree(input)
    output = sol.levelOrderBottom(root_node)
    print(output == expected)


### Example 1:
input = [3, 9, 20, None, None, 15, 7]
expected = [[15, 7], [9, 20], [3]]
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
input = [1, 2, 3, None, 4, 5, 6]
expected = [[4, 5, 6], [2, 3], [1]]
test_runner(input, expected)

### Example 5 (extra):
input = [1, 2, 3, None, None, None, 6]
expected = [[6], [2, 3], [1]]
test_runner(input, expected)

### Example 6 (extra):
input = [1, 2, None]
expected = [[2], [1]]
test_runner(input, expected)
