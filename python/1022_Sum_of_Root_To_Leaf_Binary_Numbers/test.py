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
input = [1, 0, 1, 0, 1, 0, 1]
answer = 22
root_node = sol.build_tree(input)
output = sol.sumRootToLeaf(root_node)
print(answer == output)

#### Example 2:
input = [0]
answer = 0
root_node = sol.build_tree(input)
output = sol.sumRootToLeaf(root_node)
print(answer == output)

#### Example 3 (extra):
# Single node with value 1
input = [1]
answer = 1
root_node = sol.build_tree(input)
output = sol.sumRootToLeaf(root_node)
print(answer == output)

#### Example 4 (extra):
# Unbalanced/Skewed tree (single path: 1 -> 0 -> 1 -> 1 = 11 in base 10)
input = [1, 0, None, 1, None, 1]
answer = 11
root_node = sol.build_tree(input)
output = sol.sumRootToLeaf(root_node)
print(answer == output)

#### Example 5 (extra):
# Tree with leading zeros along a path (0 -> 0 -> 1 = 1) and (0 -> 1 -> 0 = 2)
input = [0, 0, 1, None, 1, 0]
answer = 3
root_node = sol.build_tree(input)
output = sol.sumRootToLeaf(root_node)
print(answer == output)

#### Example 6 (extra):
# All 1s in a full binary tree of height 3
# Paths: (111) + (111) + (111) + (111) = 7 + 7 + 7 + 7 = 28
input = [1, 1, 1, 1, 1, 1, 1]
answer = 28
root_node = sol.build_tree(input)
output = sol.sumRootToLeaf(root_node)
print(answer == output)

#### Example 7 (extra):
# Asymmetric tree with leaves at different depths
# Path 1: 1 -> 1 -> 0 (6 in decimal)
# Path 2: 1 -> 0 (2 in decimal)
# Total sum = 6 + 2 = 8
input = [1, 1, 0, 0, None]
answer = 8
root_node = sol.build_tree(input)
output = sol.sumRootToLeaf(root_node)
print(answer == output)
