class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(" ")
        word_to_pattern = {}
        pattern_to_word = {}

        if len(pattern) != len(words):
            return False

        for i, letter in enumerate(pattern):
            word = words[i]

            if word in word_to_pattern:
                if word_to_pattern[word] != letter:
                    return False
            else:
                word_to_pattern[word] = letter

            if letter in pattern_to_word:
                if pattern_to_word[letter] != word:
                    return False
            else:
                pattern_to_word[letter] = word

        return True
