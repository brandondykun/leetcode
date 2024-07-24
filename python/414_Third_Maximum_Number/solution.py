from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = None  # highest number
        second = None  # second highest number
        third = None  # third highest number

        for num in nums:
            if num == first or num == second or num == third:
                continue
            if not first or num > first:
                third = second
                second = first
                first = num
            elif not second or num > second:
                third = second
                second = num
            elif not third or num > third:
                third = num

        return third if third != None else first
