from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        curr = []

        for num in digits:
            if not len(curr):
                curr = keypad[num]
            else:
                new = []
                for combo in curr:
                    for letter in keypad[num]:
                        new.append(f"{combo}{letter}")
                curr = new

        return curr
