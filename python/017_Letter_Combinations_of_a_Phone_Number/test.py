import pytest
from typing import List

from leetcode_utils.testing import generate_test_ids

from solution import Solution

# Test cases are (input, expected)
TEST_CASES = [
    # Example 1
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    # Example 2
    ("2", ["a", "b", "c"]),
    # 3. (extra) Single digit with 4 letters
    ("7", ["p", "q", "r", "s"]),
    # 4. (extra) Combination with 4-letter digits
    (
        "79",
        [
            "pw",
            "px",
            "py",
            "pz",
            "qw",
            "qx",
            "qy",
            "qz",
            "rw",
            "rx",
            "ry",
            "rz",
            "sw",
            "sx",
            "sy",
            "sz",
        ],
    ),
    # 5. (extra) Maximum length constraint (4 digits)
    (
        "2345",
        [
            "adgj",
            "adgk",
            "adgl",
            "adhj",
            "adhk",
            "adhl",
            "adij",
            "adik",
            "adil",
            "aegj",
            "aegk",
            "aegl",
            "aehj",
            "aehk",
            "aehl",
            "aeij",
            "aeik",
            "aeil",
            "afgj",
            "afgk",
            "afgl",
            "afhj",
            "afhk",
            "afhl",
            "afij",
            "afik",
            "afil",
            "bdgj",
            "bdgk",
            "bdgl",
            "bdhj",
            "bdhk",
            "bdhl",
            "bdij",
            "bdik",
            "bdil",
            "begj",
            "begk",
            "begl",
            "behj",
            "behk",
            "behl",
            "beij",
            "beik",
            "beil",
            "bfgj",
            "bfgk",
            "bfgl",
            "bfhj",
            "bfhk",
            "bfhl",
            "bfij",
            "bfik",
            "bfil",
            "cdgj",
            "cdgk",
            "cdgl",
            "cdhj",
            "cdhk",
            "cdhl",
            "cdij",
            "cdik",
            "cdil",
            "cegj",
            "cegk",
            "cegl",
            "cehj",
            "cehk",
            "cehl",
            "ceij",
            "ceik",
            "ceil",
            "cfgj",
            "cfgk",
            "cfgl",
            "cfhj",
            "cfhk",
            "cfhl",
            "cfij",
            "cfik",
            "cfil",
        ],
    ),
    # 6. (extra) Repeated digits
    ("22", ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]),
]

TEST_IDS = generate_test_ids(TEST_CASES)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("input, expected", TEST_CASES, ids=TEST_IDS)
def test_017(solution: Solution, input: str, expected: List[str]):
    answer = solution.letterCombinations(input)

    assert answer == expected
