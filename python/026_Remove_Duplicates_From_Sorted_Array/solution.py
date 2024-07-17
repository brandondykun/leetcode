from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_number = nums[0]
        num_removed = 0

        # replace duplicates with underscores
        for i in range(1, len(nums)):
            if nums[i] == curr_number:
                nums[i] = "_"
                num_removed += 1
            else:
                curr_number = nums[i]

        # move underscores to the end
        first_underscore_index = None
        for i in range(1, len(nums)):
            if nums[i] != "_":
                if first_underscore_index:
                    nums[first_underscore_index] = nums[i]
                    nums[i] = "_"
                    first_underscore_index += 1
            else:
                if not first_underscore_index:
                    first_underscore_index = i

        return len(nums) - num_removed
