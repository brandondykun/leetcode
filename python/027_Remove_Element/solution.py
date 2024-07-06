class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                count += 1
                for j in range(i, length):
                    if j < length - 1:
                        nums[j] = nums[j + 1]
                    else:
                        nums[j] = "_"
            else:
                i += 1

        return length - count
