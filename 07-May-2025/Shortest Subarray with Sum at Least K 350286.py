# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = n + 1
        min_heap = []
        running_sum = 0

        for i in range(n):
            running_sum += nums[i]
            if running_sum >= k:
                res = min(res, i + 1)
            
            while min_heap and running_sum - min_heap[0][0] >= k:
                _, indx = heapq.heappop(min_heap)
                res = min(res, i - indx)
            heapq.heappush(min_heap, (running_sum, i))

        return res if res <= n else -1