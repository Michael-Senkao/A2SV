# Problem: Wiggle Subsequence  - https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
    
            return n

        longest_wiggle_subsequence = 1
        increasing = False
        start = 1

        while start < n and nums[start] == nums[start - 1]:
            start += 1

        if start < n:
            increasing = True if nums[start] > nums[0] else False
        else:
            return longest_wiggle_subsequence

        start += 1
        
        for i in range(start,n):
            if increasing:
                if nums[i] < nums[i-1]:
                    longest_wiggle_subsequence += 1
                    increasing = False
            else:
                if nums[i] > nums[i - 1]:
                    longest_wiggle_subsequence += 1
                    increasing = True
            
        return longest_wiggle_subsequence + 1
