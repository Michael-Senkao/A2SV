# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        
        freq = Counter(changed)
        original = []

        if freq[0] % 2 != 0:
            return []

        original.extend([0] * (freq[0] // 2))
   
        for val in sorted(freq.keys()):
            if val == 0 or freq[val] == 0:
                continue
            
            doubled = 2 * val
            
            if freq[val] > freq[doubled]:
                return []
            
            original.extend([val] * freq[val])
            freq[doubled] -= freq[val]
        
        return original