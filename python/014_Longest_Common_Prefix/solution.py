from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        longest_prefix = len(first_word)
        curr_common = 0
        for word in strs[1:]:
            for i in range(len(word)):
                if i < len(first_word):
                    if word[i] == first_word[i]:
                        curr_common += 1
                    else:
                        break
                else:
                    break
            if curr_common < longest_prefix:
                longest_prefix = curr_common
            curr_common = 0

        if longest_prefix > 0:
            return first_word[0:longest_prefix]
        else:
            return ""
