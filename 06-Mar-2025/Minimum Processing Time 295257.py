# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        processorTime.sort()
        tasks.sort()

        maxTime = float('-inf')
        maxTaskInd = len(tasks) - 1
        for i in range(len(processorTime)):
            useTime = processorTime[i] + tasks[maxTaskInd]
            maxTime = max(maxTime, useTime)
            maxTaskInd -= 4

        return maxTime