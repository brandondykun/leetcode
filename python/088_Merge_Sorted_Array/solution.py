from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        curr = (m + n) - 1
        n1_idx = m - 1
        n2_idx = n - 1

        while curr >= 0 and n1_idx >= 0 and n2_idx >= 0:
            if nums2[n2_idx] > nums1[n1_idx]:
                nums1[curr] = nums2[n2_idx]
                n2_idx -= 1
            else:
                nums1[curr] = nums1[n1_idx]
                n1_idx -= 1

            curr -= 1

        while n2_idx >= 0:
            nums1[curr] = nums2[n2_idx]
            curr -= 1
            n2_idx -= 1
