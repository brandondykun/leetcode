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

print("Tests - 94. Binary Tree Inorder Traversal: ")

### Example 1:
input = [1, None, 2, 3]
expected = [1, 3, 2]
root_node = sol.build_tree(input)
output = sol.inorderTraversal(root_node)
print(output == expected)


## Example 2:
input = []
expected = []
root_node = sol.build_tree(input)
output = sol.inorderTraversal(root_node)
print(output == expected)

### Example 3:
input = [1]
expected = [1]
root_node = sol.build_tree(input)
output = sol.inorderTraversal(root_node)
print(output == expected)

### Example 4 (extra):
input = [1, 2, 3, None, 4, 5, 6]
expected = [2, 4, 1, 5, 3, 6]
root_node = sol.build_tree(input)
output = sol.inorderTraversal(root_node)
print(output == expected)
