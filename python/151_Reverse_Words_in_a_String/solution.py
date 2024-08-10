class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        curr = ""

        for char in s:
            if char == " ":
                if curr:
                    if output:
                        output = f"{curr} " + output
                    else:
                        output = curr
                    curr = ""
            else:
                curr += char

        if curr and output:
            return f"{curr} " + output
        elif curr:
            return curr

        return output
