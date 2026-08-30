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
# Visual Tree:
#          5
#         / \
#        4   8
#       /   / \
#      11  13  4
#     /  \    / \
#    7    2  5   1
root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
targetSum = 22
answer = [[5, 4, 11, 2], [5, 8, 4, 5]]
tree = sol.build_tree(root)
output = sol.pathSum(tree, targetSum)
print(output == answer)

#### Example 2:
# Visual Tree:
#      1
#     / \
#    2   3
root = [1, 2, 3]
targetSum = 5
answer = []
tree = sol.build_tree(root)
output = sol.pathSum(tree, targetSum)
print(output == answer)

#### Example 3:
# Visual Tree:
#      1
#     /
#    2
root = [1, 2]
targetSum = 0
answer = []
tree = sol.build_tree(root)
output = sol.pathSum(tree, targetSum)
print(output == answer)

#### Example 4 (extra): The Single Node Match
# Visual Tree:
#      3
root = [3]
targetSum = 3
answer = [[3]]
tree = sol.build_tree(root)
output = sol.pathSum(tree, targetSum)
print(output == answer)

#### Example 5 (extra): The "Zero Value" Trap
# Visual Tree:
#      1
#     / \
#    0   2
#   /
#  0
root = [1, 0, 2, 0, None, None, None]
targetSum = 1
answer = [[1, 0, 0]]
tree = sol.build_tree(root)
output = sol.pathSum(tree, targetSum)
print(output == answer)

#### Example 6 (extra): Skewed Tree (Single Line Chain)
# Visual Tree:
#       1
#      /
#     2
#    /
#   3
#  /
# 4
root = [1, 2, None, 3, None, 4, None]
targetSum = 10
answer = [[1, 2, 3, 4]]
tree = sol.build_tree(root)
output = sol.pathSum(tree, targetSum)
print(output == answer)

#### Example 7 (extra): All-Negative Numbers
# Visual Tree:
#       -2
#       / \
#    -3    -1
#      \   /
#      -5 -4
root = [-2, -3, -1, None, -5, -4, None]
targetSum = -10
answer = [[-2, -3, -5]]
tree = sol.build_tree(root)
output = sol.pathSum(tree, targetSum)
print(output == answer)

#### Example 8 (extra): Target Met Early (Not a Leaf)
# Visual Tree:
#      1
#     / \
#    4   4
#   /
#  6
root = [1, 4, 4, 6, None, None, None]
targetSum = 5
answer = [[1, 4]]  # Only the right child counts because it is a true leaf
tree = sol.build_tree(root)
output = sol.pathSum(tree, targetSum)
print(output == answer)
