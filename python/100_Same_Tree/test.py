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

print("Tests - 100. Same Tree: ")


def test_runner(tree_1: list[int], tree_2: list[int], expected: bool):
    """Helper function to test different inputs/outputs.
    Convert tree_1 list and tree_2 list to binary trees, then
    compare the two trees using isSameTree method.
    """
    p_tree = sol.build_tree(tree_1)
    q_tree = sol.build_tree(tree_2)
    output = sol.isSameTree(p_tree, q_tree)
    print(output == expected)


### Example 1:
p = [1, 2, 3]
q = [1, 2, 3]
expected = True
test_runner(p, q, expected)

### Example 2:
p = [1, 2]
q = [1, None, 2]
expected = False
test_runner(p, q, expected)

### Example 3:
p = [1, 2, 1]
q = [1, 1, 2]
expected = False
test_runner(p, q, expected)

### Example 4 (extra):
p = [1]
q = [1]
expected = True
test_runner(p, q, expected)

### Example 5 (extra):
p = []
q = []
expected = True
test_runner(p, q, expected)

### Example 6 (extra):
p = [1, 2, 3, 4, None, 6, 7, 8, 11, 13, None, 17, None, None, 23, 34, 56, 78, 100, 214]
q = [1, 2, 3, 4, None, 6, 7, 8, 11, 13, None, 17, None, None, 23, 34, 56, 78, 100, 214]
expected = True
test_runner(p, q, expected)

### Example 7 (extra):
p = [1, 2, 3, 4, None, 6, 7, 8, 11, 13, None, 17, None, None, 23, 34, 58, 78, 100, 214]
q = [1, 2, 3, 4, None, 6, 7, 8, 11, 13, None, 17, None, None, 23, 34, 56, 78, 100, 214]
expected = False
test_runner(p, q, expected)
