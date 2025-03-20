# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1), len(s2)
        if n2 < n1:
            return False

        s1Freq = Counter(s1)
        s2Freq = Counter()

        left = 0
        for i in range(len(s2)):
            char = s2[i]
            s2Freq[char] += 1
            while s2Freq[char] > s1Freq[char]:
                s2Freq[s2[left]] -= 1
                left += 1
            if s1Freq==s2Freq:
                return True

        return False
