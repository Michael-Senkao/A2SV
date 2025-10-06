# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

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
        val = ''
        for char in word:
            if char not in curr.children:
                char = '0' if char == '1' else '1'
            val += char
            curr = curr.children[char]

        return int(val, 2)


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxLen = len(bin(max(nums))[2:])
        maxV = int('1'*maxLen, 2)
        
        myTrie = Trie()
        maxXOR = 0
        
        for num in nums:
            numStr = bin(num)[2:].rjust(maxLen, '0')
            myTrie.insert(numStr)

        for num in nums:
            maxXOR = max(maxXOR, num ^ myTrie.search(bin(num ^ maxV)[2:].rjust(maxLen, '0')))
            

        return maxXOR