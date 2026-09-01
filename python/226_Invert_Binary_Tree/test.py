import pytest
from solution import Solution
from leetcode_utils.binary_tree import BinaryTreeUtil
from leetcode_utils.testing import generate_test_ids

# Test cases are (input, expected)
TEST_CASES = [
    # Example 1
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    # Example 2
    ([2, 1, 3], [2, 3, 1]),
    # Example 3
    ([], []),
    # Example 4 (extra): Left-skewed tree (becomes right-skewed)
    ([1, 2, None, 3], [1, None, 2, None, 3]),
    # Example 5 (extra): Right-skewed tree (becomes left-skewed)
    ([1, None, 2, None, 3], [1, 2, None, 3]),
    # Example 6 (extra): Single node tree
    ([1], [1]),
    # Example 7 (extra): Asymmetric tree with missing children
    ([4, 2, 7, None, 3], [4, 7, 2, None, None, 3]),
    # Example 8 (extra): Tree with duplicate and negative values
    ([0, -1, -1, 2, None, None, 2], [0, -1, -1, 2, None, None, 2]),
]

TEST_IDS = generate_test_ids(TEST_CASES)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("input_arr, expected", TEST_CASES, ids=TEST_IDS)
def test_226(solution, input_arr, expected):
    root = BinaryTreeUtil.build_tree(input_arr)
    inverted_root = solution.invertTree(root)
    actual = BinaryTreeUtil.tree_to_list_level_order(inverted_root)

    assert actual == expected
