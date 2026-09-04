import pytest
from typing import List

from leetcode_utils.binary_tree import BinaryTreeUtil
from leetcode_utils.testing import generate_test_ids

from solution import Solution

# Test cases are (input, expected)
TEST_CASES = [
    # --- Given Examples ---
    # Example 1: Standard balanced tree
    ([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
    # Example 2: Empty tree
    ([], []),
    # Example 3: Single node tree
    ([0], [0]),
    # --- Edge Cases & Structural Variants ---
    # Example 4 (extra): Left-Skewed Tree (Only left children; tests recursive shifting to right)
    ([1, 2, None, 3, None, 4], [1, None, 2, None, 3, None, 4]),
    # Example 5 (extra): Right-Skewed Tree (Already flattened; should remain unchanged)
    ([1, None, 2, None, 3, None, 4], [1, None, 2, None, 3, None, 4]),
    # Example 6 (extra): Left Heavy Subtrees (Left node has a full subtree, right is a leaf)
    ([1, 2, 5, 3, 4], [1, None, 2, None, 3, None, 4, None, 5]),
    # Example 7 (extra): Zig-Zag / Alternating Branches
    ([1, 2, None, None, 3, 4], [1, None, 2, None, 3, None, 4]),
    # Example 8 (extra): Complete 2-Level Full Binary Tree
    ([1, 2, 3], [1, None, 2, None, 3]),
    # Example 9 (extra): Values with Negative Numbers & Duplicates
    ([-10, -10, 0, 5, None, None, 2], [-10, None, -10, None, 5, None, 0, None, 2]),
]

TEST_IDS = generate_test_ids(TEST_CASES)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("input_arr, expected", TEST_CASES, ids=TEST_IDS)
def test_114(solution: Solution, input_arr: List, expected: List):
    root = BinaryTreeUtil.build_tree(input_arr)
    solution.flatten(root)
    actual = BinaryTreeUtil.tree_to_list_level_order(root)

    assert actual == expected
