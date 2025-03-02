# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        max_score = 0
        left = 0
        curr_score = 0
        window = set()

        for num in nums:
            curr_score += num
            while num in window:
                curr_score -= nums[left]
                window.remove(nums[left])
                left += 1

            max_score = max(max_score, curr_score)
            window.add(num)

        return max_score
            