from solution import Solution

sol = Solution()

#### Example 1:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
output = [1, 2, 2, 3, 5, 6]

sol.merge(nums1, m, nums2, n)
print(nums1 == output)


#### Example 2:
nums1 = [1]
m = 1
nums2 = []
n = 0
output = [1]
sol.merge(nums1, m, nums2, n)
print(nums1 == output)


#### Example 3:
nums1 = [0]
m = 0
nums2 = [1]
n = 1
output = [1]
sol.merge(nums1, m, nums2, n)
print(nums1 == output)


#### Example 4 (extra):
nums1 = [1, 3, 5, 5, 6, 8, 10, 0, 0, 0, 0, 0]
m = 7
nums2 = [2, 4, 5, 6, 9]
n = 5
output = [1, 2, 3, 4, 5, 5, 5, 6, 6, 8, 9, 10]
sol.merge(nums1, m, nums2, n)
print(nums1 == output)


#### Example 5 (extra):
nums1 = [0, 0, 0, 0, 0]
m = 0
nums2 = [1, 2, 3, 4, 5]
n = 5
output = [1, 2, 3, 4, 5]
sol.merge(nums1, m, nums2, n)
print(nums1 == output)


#### Example 6 (extra):
nums1 = [1, 0]
m = 1
nums2 = [2]
n = 1
output = [1, 2]
sol.merge(nums1, m, nums2, n)
print(nums1 == output)


#### Example 7 (extra):
nums1 = [3, 0]
m = 1
nums2 = [1]
n = 1
output = [1, 3]
sol.merge(nums1, m, nums2, n)
print(nums1 == output)
