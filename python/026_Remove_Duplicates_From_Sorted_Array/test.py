from solution import Solution


sol = Solution()

print("Tests - 26. Remove Duplicates From Sorted Array: ")

# Example 1:
nums = [1, 1, 2]
k = 2
output = [1, 2, "_"]
x = sol.removeDuplicates(nums)
print(x == k)
print(nums == output)

# Example 2:
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = 5
output = [0, 1, 2, 3, 4, "_", "_", "_", "_", "_"]
x = sol.removeDuplicates(nums)
print(x == k)
print(nums == output)

# Example 3 (extra):
nums = [-10, -5, -5, 0, 0, 5, 10]
k = 5
output = [-10, -5, 0, 5, 10, "_", "_"]
x = sol.removeDuplicates(nums)
print(x == k)
print(nums == output)

# Example 4 (extra):
nums = [2, 2, 2]
k = 1
output = [2, "_", "_"]
x = sol.removeDuplicates(nums)
print(x == k)
print(nums == output)
