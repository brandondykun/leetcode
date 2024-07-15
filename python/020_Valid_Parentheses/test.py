from solution import Solution

sol = Solution()

print("Tests - 20. Valid Parenthesis: ")

#### Example 1:
s = "()"
output = True
print(sol.isValid(s) == output)

#### Example 2:
s = "()[]{}"
output = True
print(sol.isValid(s) == output)

#### Example 3:
s = "(]"
output = False
print(sol.isValid(s) == output)

#### Example 4:
s = "[[({[})]]"
output = False
print(sol.isValid(s) == output)
