import pytest

from leetcode_utils.binary_tree import BinaryTreeUtil
from leetcode_utils.testing import generate_test_ids

from solution import Solution

# Test cases are (input, value, expected)
TEST_CASES = [
    # --- Provided Examples ---
    # Example 1
    ([4, 2, 7, 1, 3], 2, [2, 1, 3]),
    # Example 2
    ([4, 2, 7, 1, 3], 5, []),
    # --- Single Node Trees ---
    ([5], 5, [5]),  # Single node match
    ([5], 3, []),  # Single node no match (smaller)
    ([5], 8, []),  # Single node no match (larger)
    # --- Root and Leaf Matches ---
    ([4, 2, 7, 1, 3], 4, [4, 2, 7, 1, 3]),  # Target is the root
    ([4, 2, 7, 1, 3], 1, [1]),  # Target is a leaf node (left)
    ([4, 2, 7, 1, 3], 3, [3]),  # Target is a leaf node (right)
    # --- Boundary / Range Traversal Cases ---
    ([4, 2, 7, 1, 3], 0, []),  # Smaller than all values
    ([4, 2, 7, 1, 3], 10, []),  # Larger than all values
    ([10, 5, 15, 3, 7], 6, []),  # Between values in tree, not present
    # --- Skewed Trees (Degenerate BSTs) ---
    ([5, 4, None, 3, None, 2, None, 1], 2, [2, 1]),  # Left-skewed tree
    ([1, None, 2, None, 3, None, 4, None, 5], 4, [4, None, 5]),  # Right-skewed tree
    ([5, 4, None, 3], 1, []),  # Left-skewed, search fails
    ([1, None, 2, None, 3], 5, []),  # Right-skewed, search fails
]

TEST_IDS = generate_test_ids(TEST_CASES)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("input_arr, value, expected", TEST_CASES, ids=TEST_IDS)
def test_700(solution, input_arr, value, expected):
    root = BinaryTreeUtil.build_tree(input_arr)
    result = solution.searchBST(root, value)
    result_list = BinaryTreeUtil.tree_to_list_level_order(result)

    assert result_list == expected
