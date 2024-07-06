from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_majority_num = nums[0]
        current_majority_count = nums.count(nums[0])
        for num in nums:
            if num != current_majority_num:
                num_count = nums.count(num)
                if num_count > current_majority_count:
                    current_majority_num = num
                    current_majority_count = num_count
        return current_majority_num
