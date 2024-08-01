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

print("Tests - 199. Binary Tree Right Side View: ")

### Example 1:
input = [1, 2, 3, None, 5, None, 4]
expected = [1, 3, 4]
root_node = sol.build_tree(input)
output = sol.rightSideView(root_node)
print(output == expected)

## Example 2:
input = [1, None, 3]
expected = [1, 3]
root_node = sol.build_tree(input)
output = sol.rightSideView(root_node)
print(output == expected)

### Example 3:
input = []
expected = []
root_node = sol.build_tree(input)
output = sol.rightSideView(root_node)
print(output == expected)

### Example 4 (extra):
input = [1, 2, 3, None, 4, 5, 6, 7]
expected = [1, 3, 6, 7]
root_node = sol.build_tree(input)
output = sol.rightSideView(root_node)
print(output == expected)

### Example 5 (extra):
input = [1, 2, 3, None, 4, 5, 6, 7, None, None, None, None, None, 8]
expected = [1, 3, 6, 7, 8]
root_node = sol.build_tree(input)
output = sol.rightSideView(root_node)
print(output == expected)

### Example 6 (extra):
input = [1]
expected = [1]
root_node = sol.build_tree(input)
output = sol.rightSideView(root_node)
print(output == expected)

### Example 7 (extra):
input = [1, 4]
expected = [1, 4]
root_node = sol.build_tree(input)
output = sol.rightSideView(root_node)
print(output == expected)

### Example 8 (extra):
input = [1, 4, None]
expected = [1, 4]
root_node = sol.build_tree(input)
output = sol.rightSideView(root_node)
print(output == expected)
