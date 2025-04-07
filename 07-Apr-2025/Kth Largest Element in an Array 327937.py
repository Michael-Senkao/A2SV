# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for i in range(k):
            heapq.heappush(minHeap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > minHeap[0]:
                heapq.heappush(minHeap, nums[i])
                heapq.heappop(minHeap)

        return minHeap[0]