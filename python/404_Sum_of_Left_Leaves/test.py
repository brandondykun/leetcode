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
root = [3, 9, 20, None, None, 15, 7]
answer = 24
tree = sol.build_tree(root)
sum = sol.sumOfLeftLeaves(tree)
print(sum == answer)

#### Example 2:
root = [1]
answer = 0
tree = sol.build_tree(root)
sum = sol.sumOfLeftLeaves(tree)
print(sum == answer)

# Example 3: Left-Skewed Line (Only left children, but only the bottom one is a leaf)
root = [1, 2, None, 3, None, 4]
answer = 4
tree = sol.build_tree(root)
sum = sol.sumOfLeftLeaves(tree)
print(sum == answer)

# Example 4: Right-Skewed Line (Only right children, no left children exist)
root = [1, None, 2, None, 3]
answer = 0
tree = sol.build_tree(root)
sum = sol.sumOfLeftLeaves(tree)
print(sum == answer)

# Example 5: Left child that has its own children (Left non-leaf should NOT be added)
root = [1, 2, 3, 4, 5]
answer = 4
tree = sol.build_tree(root)
sum = sol.sumOfLeftLeaves(tree)
print(sum == answer)

# Example 6: Deep left leaf under a right subtree
root = [1, 2, 3, None, None, 4, None, 5]
answer = 7
tree = sol.build_tree(root)
sum = sol.sumOfLeftLeaves(tree)
print(sum == answer)

# Example 7: Negative values as left leaves
root = [0, -5, 10, None, None, -15, 20]
answer = -20
tree = sol.build_tree(root)
sum = sol.sumOfLeftLeaves(tree)
print(sum == answer)

# Example 8: Left node with right child
root = [0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8]
answer = 5
tree = sol.build_tree(root)
sum = sol.sumOfLeftLeaves(tree)
print(sum == answer)
