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

print("Tests - 257. Binary Tree Paths: ")


def test_runner(input: list[int | None], expected: list[str]):
    """Helper function to test different inputs/outputs.
    Convert input list to binary tree, run binaryTreePaths
    method and compare output to expected output.
    """
    root_node = sol.build_tree(input)
    output = sol.binaryTreePaths(root_node)
    print(output == expected)


### Example 1:
input = [1, 2, 3, None, 5]
expected = ["1->2->5", "1->3"]
test_runner(input, expected)

### Example 2:
input = [1]
expected = ["1"]
test_runner(input, expected)

### Example 3 (extra):
input = [1, 2, 3, None, 5, 6, 7, 8]
expected = ["1->2->5->8", "1->3->6", "1->3->7"]
test_runner(input, expected)

### Example 4 (extra):
input = [1, 2]
expected = ["1->2"]
test_runner(input, expected)

### Example 5 (extra):
input = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    None,
    10,
    11,
    12,
    None,
    13,
    None,
    None,
    14,
    None,
    15,
    16,
]
expected = [
    "1->2->4->8",
    "1->2->4->9->14",
    "1->2->5->10->15",
    "1->2->5->10->16",
    "1->3->6->11",
    "1->3->6->12",
    "1->3->7->13",
]
test_runner(input, expected)
