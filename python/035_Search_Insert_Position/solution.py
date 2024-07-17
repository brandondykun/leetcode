from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:
            middle = (high + low) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                high = middle - 1
            elif nums[middle] < target:
                low = middle + 1

        return low
