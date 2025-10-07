# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.isEnd = True
    
    def search(self, word):
        curr = self.root
        for char in word:
            if not curr.children[char].isEnd:
                return False
            curr = curr.children[char]
        return True

class Solution:
    def compare(self, a, b):
        if len(a) > len(b):
            return a
        if len(b) > len(a):
            return b

        return min(a, b)


    def longestWord(self, words: List[str]) -> str:
        myTrie = Trie()
        res = ''

        for word in words:
            myTrie.insert(word)

        for word in words:
            if myTrie.search(word):
                res = self.compare(res, word)

        
        return res