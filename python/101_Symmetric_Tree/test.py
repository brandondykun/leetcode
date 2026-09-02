import pytest
from typing import List

from leetcode_utils.binary_tree import BinaryTreeUtil
from leetcode_utils.testing import generate_test_ids

from solution import Solution

# Test cases are (input, expected)
TEST_CASES = [
    # Example 1
    ([1, 2, 2, 3, 4, 4, 3], True),
    # Example 2
    ([1, 2, 2, None, 3, None, 3], False),
    # 3. (extra) Single Node (Minimal tree)
    ([1], True),
    # 4. (extra) Two Nodes (Asymmetric structure)
    ([1, 2, None], False),
    # 5. (extra) Two Levels - Symmetric
    ([1, 2, 2], True),
    # 6. (extra) Two Levels - Mismatched values
    ([1, 2, 3], False),
    # 7. (extra) Mirror values with asymmetrical structure (structural check)
    ([1, 2, 2, 3, None, 3, None], False),
    # 8. (extra) Deeper Symmetric Tree (4 levels)
    ([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5], True),
    # 9. (extra) Asymmetry deep down at the leaf level
    ([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 9], False),
    # 10. (extra) All nodes share the same value (Symmetric)
    ([1, 1, 1, 1, 1, 1, 1], True),
    # 11. (extra) All same values, but asymmetric layout
    ([1, 1, 1, 1, None, 1, None], False),
    # 12. (extra) Negative values (boundary constraint check)
    ([-100, -50, -50, -1, None, None, -1], True),
]

TEST_IDS = generate_test_ids(TEST_CASES)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("input_arr, expected", TEST_CASES, ids=TEST_IDS)
def test_101(solution: Solution, input_arr: List, expected: bool):
    root = BinaryTreeUtil.build_tree(input_arr)
    answer = solution.isSymmetric(root)

    assert answer == expected
