import pytest

from leetcode_utils.testing import generate_test_ids

from solution import Solution

# Test cases are (word1, word2, expected)
TEST_CASES = [
    # Example 1
    ("abc", "pqr", "apbqcr"),
    # Example 2
    ("ab", "pqrs", "apbqrs"),
    # Example 3
    ("abcd", "pq", "apbqcd"),
    # Example 4 (extra)
    ("a", "b", "ab"),
    # Example 5 (extra)
    ("acegikmopqrstuvwxyz", "bdfhjln", "abcdefghijklmnopqrstuvwxyz"),
    # Example 6 (extra)
    ("acegi", "bdfhjklmnop", "abcdefghijklmnop"),
]

TEST_IDS = generate_test_ids(TEST_CASES)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("word1, word2, expected", TEST_CASES, ids=TEST_IDS)
def test_1786(solution: Solution, word1: str, word2: str, expected: str):
    answer = solution.mergeAlternately(word1, word2)

    assert answer == expected
