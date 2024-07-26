from solution import Solution


sol = Solution()

print("Tests - 167. Two Sum II - Input Array Is Sorted: ")

# Example 1:
numbers = [2, 7, 11, 15]
target = 9
expected = [1, 2]
output = sol.twoSum(numbers, target)
print(output == expected)

# Example 2:
numbers = [2, 3, 4]
target = 6
expected = [1, 3]
output = sol.twoSum(numbers, target)
print(output == expected)

# Example 3:
numbers = [-1, 0]
target = -1
expected = [1, 2]
output = sol.twoSum(numbers, target)
print(output == expected)

# Example 4 (extra):
numbers = [2, 5, 7, 9, 12, 27, 446, 447, 500, 10001]
target = 947
expected = [8, 9]
output = sol.twoSum(numbers, target)
print(output == expected)

# Example 5 (extra):
numbers = [-100, -90, -80, -70, -55]
target = -150
expected = [3, 4]
output = sol.twoSum(numbers, target)
print(output == expected)
