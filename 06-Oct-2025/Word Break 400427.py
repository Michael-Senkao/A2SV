# Problem: Word Break - https://leetcode.com/problems/word-break/description/

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
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.isEnd

class Solution:
    def dfs(self, i, s, memo, myTrie):
        if i == len(s):
            return True
        if i in memo:
            return memo[i]

        # Try all substrings starting from index i
        for j in range(i + 1, len(s) + 1):
            word = s[i:j]
            if myTrie.search(word) and self.dfs(j, s, memo, myTrie):
                memo[i] = True
                return True

        memo[i] = False
        return False


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        myTrie = Trie()

        for word in wordDict:
            myTrie.insert(word)

        memo = {}
        
        return self.dfs(0, s, memo, myTrie)