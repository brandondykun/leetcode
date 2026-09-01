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
root = [1, None, 0, 0, 1]
answer = [1, None, 0, None, 1]
tree = sol.build_tree(root)
output = sol.pruneTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)


#### Example 2:
root = [1, 0, 1, 0, 0, 0, 1]
answer = [1, None, 1, None, 1]
tree = sol.build_tree(root)
output = sol.pruneTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

#### Example 3:
root = [1, 1, 0, 1, 1, 0, 1, 0]
answer = [1, 1, 0, 1, 1, None, 1]
tree = sol.build_tree(root)
output = sol.pruneTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

# Test Case 4 (extra): Single node with 0
# The entire tree contains no 1s, so the root itself is pruned, returning None (empty list output).
root = [0]
answer = []
tree = sol.build_tree(root)
output = sol.pruneTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

# Test Case 5 (extra): Single node with 1
# Single-node tree containing a 1, so the root must remain intact.
root = [1]
answer = [1]
tree = sol.build_tree(root)
output = sol.pruneTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

# Test Case 6 (extra): Multi-level tree with all zeros
# Verifies that a multi-level tree with only 0s prunes every node back up to the root.
root = [0, 0, 0, None, 0, 0, None]
answer = []
tree = sol.build_tree(root)
output = sol.pruneTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

# Test Case 7 (extra): All ones in a tree
# Verifies that no nodes are pruned when every node value is 1.
root = [1, 1, 1, 1, 1]
answer = [1, 1, 1, 1, 1]
tree = sol.build_tree(root)
output = sol.pruneTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

# Test Case 8 (extra): Entire left subtree is zeros, right subtree has a 1
# Tests complete pruning of an entire major sub-branch while preserving the path to a valid node.
root = [1, 0, 0, 0, 0, None, 1]
answer = [1, None, 0, None, 1]
tree = sol.build_tree(root)
output = sol.pruneTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)

# Test Case 9 (extra): Deep chain of zeros leading to a 1 at the bottom
# Tests that intermediate 0-value nodes are NOT pruned if they are ancestors of a node with 1.
root = [0, 0, None, 0, None, 1]
answer = [0, 0, None, 0, None, 1]
tree = sol.build_tree(root)
output = sol.pruneTree(tree)
output_list = sol.tree_to_list_level_order(output)
print(output_list == answer)
