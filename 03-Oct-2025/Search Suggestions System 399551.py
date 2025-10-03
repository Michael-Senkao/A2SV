# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = set()
        self.isEnd = True

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr.children[char].words.add(word)
            curr = curr.children[char]

        curr.isEnd = True

    



class Solution:
    def __init__(self):
        self.res = []
        
    def printWords(self, curr, searchWord, i):
        if i >= len(searchWord):
            return
        if searchWord[i] not in curr.children:
            for j in range(i, len(searchWord)):
                self.res.append([])

            return
        
        self.res.append(sorted(curr.children[searchWord[i]].words)[:3])
        self.printWords(curr.children[searchWord[i]], searchWord, i + 1)

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        trie = Trie()
        for product in products:
            trie.insert(product)

  
        self.printWords(trie.root, searchWord, 0)
            
        return self.res
        