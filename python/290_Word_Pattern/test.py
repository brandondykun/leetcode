from solution import Solution

sol = Solution()


# Example 1:
pattern = "abba"
s = "dog cat cat dog"
answer = True
output = sol.wordPattern(pattern, s)
print(answer == output)

# Example 2:
pattern = "abba"
s = "dog cat cat fish"
answer = False
output = sol.wordPattern(pattern, s)
print(answer == output)

# Example 3:
pattern = "aaaa"
s = "dog cat cat dog"
answer = False
output = sol.wordPattern(pattern, s)
print(answer == output)

# Example 4 (extra):
pattern = "a"
s = "mouse"
answer = True
output = sol.wordPattern(pattern, s)
print(answer == output)

# Example 5 (extra):
pattern = "abcde"
s = "mouse cat dog rabbit bird"
answer = True
output = sol.wordPattern(pattern, s)
print(answer == output)

# Example 6 (extra):
pattern = "abcdeafgc"
s = "mouse cat dog rabbit bird mouse pig cow dog"
answer = True
output = sol.wordPattern(pattern, s)
print(answer == output)

# Example 7 (extra)
pattern = "aaa"
s = "aa aa aa aa"
answer = False
output = sol.wordPattern(pattern, s)
print(answer == output)
