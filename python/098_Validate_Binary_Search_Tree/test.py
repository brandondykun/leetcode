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

print("Tests - 98. Validate Binary Search Tree: ")


#### Example 1:
input = [2, 1, 3]
expected = True
root_node = sol.build_tree(input)
output = sol.isValidBST(root_node)
print(output == expected)


#### Example 2:
input = [5, 1, 4, None, None, 3, 6]
expected = False
root_node = sol.build_tree(input)
output = sol.isValidBST(root_node)
print(output == expected)

#### Example 3 (extra):
input = [5]
expected = True
root_node = sol.build_tree(input)
output = sol.isValidBST(root_node)
print(output == expected)

#### Example 4 (extra):
input = [4, 2]
expected = True
root_node = sol.build_tree(input)
output = sol.isValidBST(root_node)
print(output == expected)

#### Example 5 (extra):
input = [4, 5]
expected = False
root_node = sol.build_tree(input)
output = sol.isValidBST(root_node)
print(output == expected)
