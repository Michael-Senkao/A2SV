# Problem: Maximum Sum of Distinct Subarrays With Length K - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = set()

        maxSum = 0
        left = 0
        sum = 0
        for right, num in enumerate(nums):
            sum += num
            while num in window or right - left + 1 > k:
                sum -= nums[left]
                window.remove(nums[left])
                left += 1

            window.add(num)
            if right - left + 1 == k:
                maxSum = max(maxSum, sum)
        return maxSum