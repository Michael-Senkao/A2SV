# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        windowSum = 0
        minSize = n + 1

        for right in range(n):
            windowSum += nums[right]

            if windowSum >= target:
                while windowSum >= target:
                    windowSum -= nums[left]
                    left += 1

                minSize = min(minSize, right - left + 2)

        return minSize if minSize <= n else 0