from solution import TreeNode, Solution
from collections import deque


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

    def tree_to_list_level_order(self, root: TreeNode) -> list[int]:
        """Level-Order Traversal: Layer by layer from top to bottom"""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Trim trailing None values from the list
        while result and result[-1] is None:
            result.pop()

        return result


sol = TestHelper()


#### Example 1:
root = [4, 2, 7, 1, 3, 6, 9]
answer = [4, 7, 2, 9, 6, 3, 1]
tree = sol.build_tree(root)
output = sol.invertTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

#### Example 2:
root = [2, 1, 3]
answer = [2, 3, 1]
tree = sol.build_tree(root)
output = sol.invertTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

#### Example 3:
root = []
answer = []
tree = sol.build_tree(root)
output = sol.invertTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

#### Example 4 (extra): Left-skewed tree (becomes right-skewed)
root = [1, 2, None, 3]
answer = [1, None, 2, None, 3]
tree = sol.build_tree(root)
output = sol.invertTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

### Example 5 (extra): Right-skewed tree (becomes left-skewed)
root = [1, None, 2, None, 3]
answer = [1, 2, None, 3]
tree = sol.build_tree(root)
output = sol.invertTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

#### Example 6 (extra): Single node tree
root = [1]
answer = [1]
tree = sol.build_tree(root)
output = sol.invertTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

#### Example 7 (extra): Asymmetric tree with missing children
root = [4, 2, 7, None, 3]
answer = [4, 7, 2, None, None, 3]
tree = sol.build_tree(root)
output = sol.invertTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

#### Example 8 (extra): Tree with duplicate and negative values
root = [0, -1, -1, 2, None, None, 2]
answer = [0, -1, -1, 2, None, None, 2]
tree = sol.build_tree(root)
output = sol.invertTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)
