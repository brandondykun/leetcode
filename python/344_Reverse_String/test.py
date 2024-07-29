from solution import Solution

sol = Solution()

print("Tests - 344. Reverse String: ")

#### Example 1:
s = ["h", "e", "l", "l", "o"]
expected = ["o", "l", "l", "e", "h"]
sol.reverseString(s)
print(s == expected)

#### Example 2:
s = ["H", "a", "n", "n", "a", "h"]
expected = ["h", "a", "n", "n", "a", "H"]
sol.reverseString(s)
print(s == expected)

#### Example 3 (extra):
s = ["T"]
expected = ["T"]
sol.reverseString(s)
print(s == expected)

#### Example 4 (extra):
s = ["s", "b"]
expected = ["b", "s"]
sol.reverseString(s)
print(s == expected)
