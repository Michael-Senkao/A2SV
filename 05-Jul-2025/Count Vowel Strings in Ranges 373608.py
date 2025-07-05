# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefixSum = [0] * n
        vowels = 'aeiou'
        res = []

        prefixSum[0] = 1 if words[0][0] in vowels and words[0][-1] in vowels else 0

        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + (words[i][0] in vowels and words[i][-1] in vowels)
        
        for l,r in queries:
            res.append(prefixSum[r])
            if l > 0:
                res[-1] -= prefixSum[l - 1]
        return res