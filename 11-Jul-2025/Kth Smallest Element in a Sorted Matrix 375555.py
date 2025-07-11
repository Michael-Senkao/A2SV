# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        for i in range(n):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))
        
        while k > 1:
            _, mat_indx, curr_indx = heapq.heappop(min_heap)
            curr_indx += 1
            if curr_indx < len(matrix[mat_indx]):
                heapq.heappush(min_heap, (matrix[mat_indx][curr_indx], mat_indx, curr_indx))
            k -= 1

        return min_heap[0][0]