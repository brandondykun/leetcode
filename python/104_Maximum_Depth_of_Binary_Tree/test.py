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

print("Tests - 104. Maximum Depth of Binary Tree: ")

### Example 1:
root = [3, 9, 20, None, None, 15, 7]
expected = 3
root_node = sol.build_tree(root)
output = sol.maxDepth(root_node)
print(output == expected)

### Example 2:
root = [1, None, 2]
expected = 2
root_node = sol.build_tree(root)
output = sol.maxDepth(root_node)
print(output == expected)

### Example 3 (extra):
root = [1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, None, 9]
expected = 5
root_node = sol.build_tree(root)
output = sol.maxDepth(root_node)
print(output == expected)

### Example 4 (extra):
root = []
expected = 0
root_node = sol.build_tree(root)
output = sol.maxDepth(root_node)
print(output == expected)
