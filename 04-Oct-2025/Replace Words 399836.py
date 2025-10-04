# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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
        root = []
        for char in word:
            if char not in curr.children:
                break
            root.append(char)
            curr = curr.children[char]
            if curr.isEnd:
                break
            
        if not word or not curr.isEnd:
            return word

        return ''.join(root)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        myTrie = Trie()
        res = []

        for word in dictionary:
            myTrie.insert(word)
        
        for word in sentence.split():
            res.append(myTrie.search(word))

        return ' '.join(res)