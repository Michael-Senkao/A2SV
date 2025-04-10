# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        prefixCost = {}
        minOperations = float('inf')
       
        runningSum = 0
        for index, num in enumerate(nums):
            runningSum += num
            prefixCost[runningSum] = index
            if runningSum == x:
                minOperations = index + 1

        
        runningSum = 0
        for index in range(n - 1, -1, -1):
            runningSum += nums[index]
            if runningSum == x:
                minOperations = min(minOperations, n - index)
            elif x - runningSum in prefixCost:
                if prefixCost[x - runningSum] < index:
                    minOperations = min(minOperations, prefixCost[x - runningSum] + n - index + 1)


        return minOperations if minOperations != float('inf') else -1