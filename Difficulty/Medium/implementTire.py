#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.isEnd = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for s in word:
            s_index = ord(s) - ord("a")
            if not node.children[s_index]:
                node.children[s_index]=Trie()
            node = node.children[s_index]
        node.isEnd=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for s in word:
            s_index = ord(s) - ord("a")
            if not node.children[s_index]:
                return False
            else:
                node = node.children[s_index]
        return True if node.isEnd is True else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for s in prefix:
            s_index = ord(s) - ord("a")
            if not node.children[s_index]:
                return False
            else:
                node = node.children[s_index]
        return True