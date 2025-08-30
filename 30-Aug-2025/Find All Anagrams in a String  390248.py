# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        freqP = Counter(p)
        windowFreq = Counter()
        res = []

        left = 0
        for right in range(n):
            if s[right] not in freqP:
                # Remove unwanted characters from the window
                while left < right:
                    windowFreq[s[left]] -= 1

                    left += 1
                left += 1 
            else:
                windowFreq[s[right]] += 1
                while windowFreq[s[right]] > freqP[s[right]]:
                    
                    windowFreq[s[left]] -= 1

                    left += 1
                
                if windowFreq == freqP:
                    res.append(left)
        
        return res