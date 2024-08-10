from solution import Solution

sol = Solution()

print("Tests - 151. Reverse Words in a String: ")


#### Example 1:
s = "the sky is blue"
expected = "blue is sky the"
output = sol.reverseWords(s)
print(output == expected)

#### Example 2:
s = "  hello world  "
expected = "world hello"
output = sol.reverseWords(s)
print(output == expected)

#### Example 3:
s = "a good   example"
expected = "example good a"
output = sol.reverseWords(s)
print(output == expected)

#### Example 4 (extra):
s = " a "
expected = "a"
output = sol.reverseWords(s)
print(output == expected)

#### Example 5 (extra):
s = "b"
expected = "b"
output = sol.reverseWords(s)
print(output == expected)
