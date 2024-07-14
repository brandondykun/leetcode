from solution import Solution

sol = Solution()

print("Tests - 9. Palindrome Number: ")

#### Example 1:
x = 121
output = True
print(sol.isPalindrome(x) == output)

#### Example 2:
x = -121
output = False
print(sol.isPalindrome(x) == output)

#### Example 3:
x = 10
output = False
print(sol.isPalindrome(x) == output)

#### Example 4 (extra):
x = 1122332211
output = True
print(sol.isPalindrome(x) == output)
