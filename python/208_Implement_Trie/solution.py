class Node(object):
    def __init__(self):
        self.children = {}
        self.is_word_end = False


class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for letter in word:
            if curr.children.get(letter, None):
                curr = curr.children[letter]
            else:
                curr.children[letter] = Node()
                curr = curr.children[letter]

        curr.is_word_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for letter in word:
            if curr.children.get(letter, None):
                curr = curr.children[letter]
            else:
                return False

        if curr.is_word_end:
            return True
        return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for letter in prefix:
            if curr.children.get(letter, None):
                curr = curr.children[letter]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
word = "hello"
obj = Trie()
obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# print(obj.search("hello"))
print(obj.startsWith("ha"))
