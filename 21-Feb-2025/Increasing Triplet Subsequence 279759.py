# Problem: Increasing Triplet Subsequence - https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first_min, second_min = float('inf'), float('inf')


        curr_first,curr_second = float('inf'), float('inf')


        for num in nums:
            if num > second_min:
                return True
            if num < curr_first:
                curr_first = num
                curr_second = float('inf')
            elif num != curr_first and num < curr_second:
                curr_second = num
                first_min,second_min = curr_first, curr_second

        return False