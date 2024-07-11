from solution import Solution

sol = Solution()

#### Example 1:
strs = ["flower", "flow", "flight"]
output = "fl"
print(sol.longestCommonPrefix(strs) == output)


#### Example 2:
strs = ["dog", "racecar", "car"]
output = ""
print(sol.longestCommonPrefix(strs) == output)


#### Example 3 (extra):
strs = ["through", "throw", "thrown", "throughout"]
output = "thro"
print(sol.longestCommonPrefix(strs) == output)
