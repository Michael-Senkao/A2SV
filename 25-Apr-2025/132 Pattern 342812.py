# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        minHeapRight = []
        minLeft = []
        currMin = float('inf')
        
        # Compute the minimun value to the left of each element
        for num in nums:
            minLeft.append(currMin)
            currMin = min(currMin, num)
        
        # Push the last element initially to the min heap
        heapq.heappush(minHeapRight, nums[-1])
        
        # Assume each index between 1 and n - 2 to be the peak
        for i in range(n-2, 0, -1):
            while minHeapRight and minHeapRight[0] <= minLeft[i]:
                heapq.heappop(minHeapRight)
            
            if minHeapRight and minLeft[i] < minHeapRight[0] < nums[i]:
                return True # Answer found
            # Push the current element to the heap
            heapq.heappush(minHeapRight, nums[i])

        return False