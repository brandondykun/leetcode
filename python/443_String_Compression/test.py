import pytest
from typing import List

from leetcode_utils.testing import generate_test_ids

from solution import Solution

# Test cases are (input_list, expected_length, expected_list)
TEST_CASES = [
    # Example 1
    (["a", "a", "b", "b", "c", "c", "c"], 6, ["a", "2", "b", "2", "c", "3"]),
    # Example 2
    (["a"], 1, ["a"]),
    # Example 3
    (
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
        4,
        ["a", "b", "1", "2"],
    ),
    # Test 4 (extra) # Fails without `chars[write] = current_char`: write lags behind read, leaving leftover 'a' at chars[2] instead of 'b':
    (["a", "a", "a", "b"], 3, ["a", "3", "b"]),
    # Test 5 (extra) Multi-digit count causing significant index drift (count >= 10):
    (
        ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "b", "b"],
        5,
        ["a", "1", "0", "b", "2"],
    ),
    # Test 6 (extra) Large multi-digit count at the very end of the array (count >= 100):
    (["a"] * 12, 3, ["a", "1", "2"]),
    # Test 7 (extra): All distinct single characters (count is always 1):
    (["a", "b", "c", "d"], 4, ["a", "b", "c", "d"]),
    # Test 8 (extra) Alternating single characters (tests write/read staying in sync):
    (["a", "b", "a", "b"], 4, ["a", "b", "a", "b"]),
    # Test 9 (extra) Mixed single characters and multi-digit counts:
    (
        ["a", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
        5,
        ["a", "b", "c", "1", "2"],
    ),
    # Test 10 (extra) Non-letter symbols and numbers as character elements:
    (["1", "1", "2", "#", "#", "#"], 5, ["1", "2", "2", "#", "3"]),
]

TEST_IDS = generate_test_ids(TEST_CASES)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("input_list, length, expected_list", TEST_CASES, ids=TEST_IDS)
def test_443(
    solution: Solution, input_list: List, length: int, expected_list: List[str]
):
    answer = solution.compress(input_list)

    assert input_list[:length] == expected_list
    assert answer == length
