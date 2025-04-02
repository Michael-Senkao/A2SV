# Problem: Smallest Range Covering Elements from K Lists - https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        minHeap = []
        currMax = float('-inf')

        for i, num in enumerate(nums):
            heapq.heappush(minHeap, (num[0], i, 0))
            currMax = max(currMax, num[0])

        smallestRange = float('inf')
        start,end = -1,-1

        while len(minHeap) == k:
            val, numsInd, listInd = heapq.heappop(minHeap)

            if currMax - val < smallestRange:
                smallestRange = currMax - val
                start,end = val, currMax

            listInd += 1
            if listInd < len(nums[numsInd]):
                heapq.heappush(minHeap, (nums[numsInd][listInd], numsInd, listInd))
                currMax = max(currMax, nums[numsInd][listInd])


        return [start, end]
        