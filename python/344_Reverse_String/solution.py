from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        iterations = len(s) // 2

        for i in range(iterations):
            temp = s[i]
            opposite_index = (i + 1) * -1

            s[i], s[opposite_index] = s[opposite_index], temp
