# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n < k:
            return 0

        currSum = sum(nums[:k]) # Sum of first k elements
        maxAvg = currSum / k # Average of first k elements

        # Iterate through the remaining n - k elements
        for i in range(k, n):
            currSum += nums[i] # Add current element to the window
            currSum -= nums[i - k] # Remove last element from the window

            maxAvg = max(maxAvg, currSum / k) # Update the maximum average so far

        return maxAvg
        