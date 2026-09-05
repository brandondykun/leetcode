class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        output = ""
        word1_len = len(word1)
        word2_len = len(word2)

        while index < word1_len or index < word2_len:
            if index < word1_len:
                output += word1[index]

            if index < word2_len:
                output += word2[index]

            index += 1

        return output
