# Problem: Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                num += 1

                while num in nums_set:
                    count += 1
                    num += 1

                res = max(res, count)

        return res