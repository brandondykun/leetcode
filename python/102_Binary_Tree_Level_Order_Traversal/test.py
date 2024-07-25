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

print("Tests - 102. Binary Tree Level Order Traversal: ")

### Example 1:
input = [3, 9, 20, None, None, 15, 7]
expected = [[3], [9, 20], [15, 7]]
root_node = sol.build_tree(input)
output = sol.levelOrder(root_node)
print(output == expected)

## Example 2:
input = [1]
expected = [[1]]
root_node = sol.build_tree(input)
output = sol.levelOrder(root_node)
print(output == expected)

### Example 3:
input = []
expected = []
root_node = sol.build_tree(input)
output = sol.levelOrder(root_node)
print(output == expected)

### Example 4 (extra):
input = [1, 2, 3, None, 4, 5, 6]
expected = [[1], [2, 3], [4, 5, 6]]
root_node = sol.build_tree(input)
output = sol.levelOrder(root_node)
print(output == expected)

### Example 5 (extra):
input = [1, 2, 3, None, None, None, 6]
expected = [[1], [2, 3], [6]]
root_node = sol.build_tree(input)
output = sol.levelOrder(root_node)
print(output == expected)

### Example 6 (extra):
input = [1, 2, None]
expected = [[1], [2]]
root_node = sol.build_tree(input)
output = sol.levelOrder(root_node)
print(output == expected)
