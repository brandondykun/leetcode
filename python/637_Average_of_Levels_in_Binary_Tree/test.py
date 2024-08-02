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

print("Tests - 637. Average of Levels in Binary Tree: ")

### Example 1:
input = [3, 9, 20, None, None, 15, 7]
expected = [3.00000, 14.50000, 11.00000]
root_node = sol.build_tree(input)
output = sol.averageOfLevels(root_node)
print(output == expected)

## Example 2:
input = [3, 9, 20, 15, 7]
expected = [3.00000, 14.50000, 11.00000]
root_node = sol.build_tree(input)
output = sol.averageOfLevels(root_node)
print(output == expected)

## Example 3 (extra):
input = [3, 5, 20, 2, 4, 8, 12, 9, 13]
expected = [3.00000, 12.50000, 6.5, 11]
root_node = sol.build_tree(input)
output = sol.averageOfLevels(root_node)
print(output == expected)

### Example 4 (extra):
input = [1]
expected = [1]
root_node = sol.build_tree(input)
output = sol.averageOfLevels(root_node)
print(output == expected)

### Example 5 (extra):
input = [1, 3, None]
expected = [1, 3]
root_node = sol.build_tree(input)
output = sol.averageOfLevels(root_node)
print(output == expected)

### Example 5 (extra):
input = [1, 3, None, 5, None, 9]
expected = [1, 3, 5, 9]
root_node = sol.build_tree(input)
output = sol.averageOfLevels(root_node)
print(output == expected)
