from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        print(nums_sorted)
        start_index = 0
        end_index = len(nums) - 1
        while start_index < end_index:
            current_sum = nums_sorted[start_index] + nums_sorted[end_index]
            if current_sum == target:
                num_1_index = nums.index(nums_sorted[start_index])
                num_2_index = nums.index(nums_sorted[end_index])
                if num_1_index == num_2_index:
                    num_2_index = (
                        nums[num_1_index + 1 :].index(nums_sorted[end_index])
                        + num_1_index
                        + 1
                    )
                return [num_1_index, num_2_index]
            elif current_sum > target:
                end_index -= 1
            else:
                start_index += 1
