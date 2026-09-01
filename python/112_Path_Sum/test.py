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


#### Example 1:
root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
targetSum = 22
answer = True
tree = sol.build_tree(root)
output = sol.hasPathSum(tree, targetSum)
print(output == answer)

#### Example 2:
root = [1, 2, 3]
targetSum = 5
answer = False
tree = sol.build_tree(root)
output = sol.hasPathSum(tree, targetSum)
print(output == answer)

#### Example 3:
root = []
targetSum = 0
answer = False
tree = sol.build_tree(root)
output = sol.hasPathSum(tree, targetSum)
print(output == answer)

#### Example 4 (extra):
root = [5]
targetSum = 5
answer = True
tree = sol.build_tree(root)
output = sol.hasPathSum(tree, targetSum)
print(output == answer)

#### Example 5 (extra):
root = [5]
targetSum = 3
answer = False
tree = sol.build_tree(root)
output = sol.hasPathSum(tree, targetSum)
print(output == answer)

#### Example 6 (extra):
root = [1, 2]
targetSum = 1
answer = False
tree = sol.build_tree(root)
output = sol.hasPathSum(tree, targetSum)
print(output == answer)
