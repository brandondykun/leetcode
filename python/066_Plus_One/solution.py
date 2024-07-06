from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr = len(digits) - 1

        while curr >= 0:
            if digits[curr] == 9:
                digits[curr] = 0
                curr -= 1
            else:
                digits[curr] = digits[curr] + 1
                return digits

        digits.insert(0, 1)
        return digits


arr = [0]
sol = Solution()

print(sol.plusOne(arr))
