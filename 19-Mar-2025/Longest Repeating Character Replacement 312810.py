# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        res = 0
        maxFreq = 0
        totalFreq = 0

        left = 0
        for right in range(len(s)):
            totalFreq += 1
            freq[s[right]] += 1
            maxFreq = max(maxFreq, freq[s[right]])
            while totalFreq - maxFreq > k:
                totalFreq -= 1
                freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res