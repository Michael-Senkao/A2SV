# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def notSame(word1, word2):
            for char in word1:
                if char in word2:
                    return False
            return True


        n = len(words)
        word_sets = [set(word) for word in words]
        res = 0

        for i in range(len(words)):
            for j in range(i + 1, n):
                if notSame(word_sets[i], word_sets[j]):
                    res = max(res, len(words[i]) * len(words[j]))

        return res