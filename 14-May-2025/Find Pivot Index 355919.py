# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        n = len(nums)
        prefix_sum = []
        running_sum = 0
        res = -1

        for num in nums:
            prefix_sum.append(running_sum)
            running_sum += num

        suffix_sum = 0
        for i in range(n - 1, -1, -1):
            if suffix_sum == prefix_sum[i]:
                res = i
            suffix_sum += nums[i]
        
        return res