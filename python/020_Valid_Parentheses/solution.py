class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for i in range(len(s)):
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                lst.append(s[i])
                continue
            if not len(lst) or s[i] == "]" and lst[-1] != "[":
                return False
            elif not len(lst) or s[i] == ")" and lst[-1] != "(":
                return False
            elif not len(lst) or s[i] == "}" and lst[-1] != "{":
                return False
            lst.pop()
        return len(lst) == 0
