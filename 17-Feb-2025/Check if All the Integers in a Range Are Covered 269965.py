# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        n = min(right + 1, 51)
        prefix_range = [0]*n

        for start, end in ranges:
            if start < n:
                prefix_range[start] += 1
            if end + 1 < n:
                prefix_range[end + 1] -= 1

        for i in range(1, n):
            prefix_range[i] += prefix_range[i - 1]

        for i in range(left, right + 1):

            if prefix_range[i] < 1:
                return False

        return True