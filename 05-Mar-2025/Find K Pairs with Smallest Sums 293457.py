# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/


import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        
        n1,n2 = len(nums1),len(nums2)
        
        res = [[]]*k # Stores the result
        curr_index = 0 # Tracks the index to add the current smallest pair_sum

        # Create a heap that stores the ith index of nums1 with the 0th index in nums2
        min_heap = [] # To get the smallest pair sum efficiently
        for i in range(n1):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        # Find the k pairs with smallest sum
        for _ in range(k):
            # Get the smallest pair
            min_pair_sum, nums1_index, nums2_index = heapq.heappop(min_heap)
            
            res[curr_index] = [nums1[nums1_index], nums2[nums2_index]]
            curr_index += 1

            # Go to the next index in nums2
            if nums2_index < n2 - 1:
                heapq.heappush(min_heap, (nums1[nums1_index] + nums2[nums2_index + 1], nums1_index,nums2_index + 1))
        return res