from solution import Solution

sol = Solution()

print("Tests - 414. Third Maximum Number: ")

#### Example 1:
input = [3, 2, 1]
expected = 1
output = sol.thirdMax(input)
print(output == expected)

#### Example 2:
input = [1, 2]
expected = 2
output = sol.thirdMax(input)
print(output == expected)

#### Example 3:
input = [2, 2, 3, 1]
expected = 1
output = sol.thirdMax(input)
print(output == expected)

#### Example 4 (extra):
input = [1, 3, 5, 6, 8, 9, 10, 11, 13, 17, 26, 30, 32]
expected = 26
output = sol.thirdMax(input)
print(output == expected)

#### Example 5 (extra):
input = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
expected = 1
output = sol.thirdMax(input)
print(output == expected)

#### Example 6 (extra):
input = [3, 2, 1, 2, 1, 3]
expected = 1
output = sol.thirdMax(input)
print(output == expected)

#### Example 7 (extra):
input = [-2147483648, 1, 2]
expected = -2147483648
output = sol.thirdMax(input)
print(output == expected)

#### Example 8 (extra):
input = [-3, -2, -1, -2, -3]
expected = -3
output = sol.thirdMax(input)
print(output == expected)

#### Example 9 (extra):
input = [1, 2147483647, -2147483648]
expected = -2147483648
output = sol.thirdMax(input)
print(output == expected)

#### Example 10 (extra):
input = [3, 3, 4, 3, 4, 3, 0, 3, 3]
expected = 0
output = sol.thirdMax(input)
print(output == expected)
