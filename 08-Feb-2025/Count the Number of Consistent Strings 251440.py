# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        consistent_count = 0
        for word in words:
            for char in word:
                if char not in allowed_set:
                    break
            else:
                consistent_count += 1
        
        return consistent_count