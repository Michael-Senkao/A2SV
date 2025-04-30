# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        increasing = deque()
        decreasing = deque()
        left = 0
        res = 0

        for right in range(n):
            while increasing and nums[increasing[-1]] > nums[right]:
                increasing.pop()
            increasing.append(right)

            while decreasing and nums[decreasing[-1]] < nums[right]:
                decreasing.pop()
            decreasing.append(right)

            while increasing and decreasing and nums[decreasing[0]] - nums[increasing[0]] > 2:
                if decreasing[0] < increasing[0]:
                    left = decreasing[0] + 1
                    decreasing.popleft()
                else:
                   left = increasing[0] + 1
                   increasing.popleft() 

            res += right - left + 1

        return res
        