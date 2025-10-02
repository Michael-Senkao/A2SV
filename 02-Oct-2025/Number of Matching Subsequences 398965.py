# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def isSub(self, word, s, char_indx):
        prev = -1

        for i,char in enumerate(word):
            if char not in char_indx or char_indx[char][-1] <= prev:
                return False

            prev = self.findNext(prev, char_indx[char])
        

        return True
    
    def findNext(self, prev, char_indx):
        indx = char_indx[-1]
        left, right = 0, len(char_indx) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if char_indx[mid] <= prev:
                left = mid + 1
            else:
                indx = mid
                right = mid - 1

        return char_indx[indx]


    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_indx = defaultdict(list)
        res = 0

        for indx, char in enumerate(s):
            char_indx[char].append(indx)

        for word in words:
            if self.isSub(word, s, char_indx):
                res += 1

        return res