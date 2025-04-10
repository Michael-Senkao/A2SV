# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        leftCount = leftSum = 0
        rightCount, rightSum = n, sum(nums)
        
        
        minAvgIndex = -1
        minAvgDiff = float('inf')

        
        for i in range(n-1):
            leftCount += 1
            leftSum += nums[i]

            rightCount -= 1
            rightSum -= nums[i]

            avgLeft = leftSum // leftCount
            avgRight = rightSum // rightCount
            avgDiff = abs(avgRight - avgLeft)
            
            if avgDiff == 0:
                return i

            if avgDiff < minAvgDiff:
                minAvgDiff, minAvgIndex = avgDiff, i
            
        leftSum += nums[-1]
        if leftSum // n < minAvgDiff:
            minAvgIndex = n - 1
        return minAvgIndex