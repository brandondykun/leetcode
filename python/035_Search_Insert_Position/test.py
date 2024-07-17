from solution import Solution

sol = Solution()

print("Tests - 35. Search Insert Position: ")

#### Example 1:
nums = [1, 3, 5, 6]
target = 5
expected = 2
output = sol.searchInsert(nums, target)
print(output == expected)

#### Example 2:
nums = [1, 3, 5, 6]
target = 2
expected = 1
output = sol.searchInsert(nums, target)
print(output == expected)

#### Example 3:
nums = [1, 3, 5, 6]
target = 7
expected = 4
output = sol.searchInsert(nums, target)
print(output == expected)

#### Example 4 (extra):
nums = [1, 3, 5, 6, 8, 9, 10, 11, 13, 17, 26, 30, 32]
target = 14
expected = 9
output = sol.searchInsert(nums, target)
print(output == expected)

#### Example 5 (extra):
nums = [0]
target = 0
expected = 0
output = sol.searchInsert(nums, target)
print(output == expected)

#### Example 6 (extra):
nums = [0, 1, 2, 3, 4, 5, 6, 7]
target = 7
expected = 7
output = sol.searchInsert(nums, target)
print(output == expected)
