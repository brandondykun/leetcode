import pytest
from typing import List

from leetcode_utils.linked_list import LinkedListUtil
from leetcode_utils.testing import generate_test_ids

from solution import Solution

# Test cases are (input, expected)
TEST_CASES = [
    # Example 1
    ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
    # Example 2
    ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
    # --- Edge Cases & Edge Conditions ---
    # 1. Empty List (0 nodes)
    ([], []),
    # 2. Single Node (1 node)
    ([1], [1]),
    # 3. Two Nodes (Minimal odd + even pair)
    ([1, 2], [1, 2]),
    # 4. Three Nodes (Minimal non-trivial reordering)
    ([1, 2, 3], [1, 3, 2]),
    # 5. Four Nodes (Even length boundary)
    ([1, 2, 3, 4], [1, 3, 2, 4]),
    # --- Special Value Patterns ---
    # 6. Duplicate values to ensure nodes are grouped by position, not value
    ([2, 2, 2, 2], [2, 2, 2, 2]),
    # 7. Negative numbers and zero
    ([-1, 0, -2, 5, -3], [-1, -2, -3, 0, 5]),
]

TEST_IDS = generate_test_ids(TEST_CASES)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("input_arr, expected", TEST_CASES, ids=TEST_IDS)
def test_328(solution: Solution, input_arr: List, expected: bool):
    root = LinkedListUtil.build_list(input_arr)
    answer = solution.oddEvenList(root)
    answer_list = LinkedListUtil.to_list(answer)

    assert answer_list == expected
