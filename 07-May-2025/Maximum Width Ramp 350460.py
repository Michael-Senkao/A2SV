# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        maxWidth = 0
        stack = []
        ans = 0

        for indx, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(indx)

        right = n-1
        while stack:
            top = stack.pop()
            while nums[right] < nums[top]:
                right -= 1
            ans = max(ans, right - top)
        return ans