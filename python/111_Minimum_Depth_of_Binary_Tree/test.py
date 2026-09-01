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


def test_runner(input: list[int | None], expected: bool):
    """Helper function to test different inputs/outputs.
    Convert input list to binary tree, calls isBalanced
    method, compares output to expected output boolean.
    """
    root_node = sol.build_tree(input)
    output = sol.minDepth(root_node)
    print(output == expected)


#### Example 1:
input = [3, 9, 20, None, None, 15, 7]
expected = 2
test_runner(input, expected)

#### Example 2:
input = [2, None, 3, None, 4, None, 5, None, 6]
expected = 5
test_runner(input, expected)

#### Example 3 (extra):
input = [2]
expected = 1
test_runner(input, expected)

#### Example 4 (extra):
input = [2, 3, 4]
expected = 2
test_runner(input, expected)
