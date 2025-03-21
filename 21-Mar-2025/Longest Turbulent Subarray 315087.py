# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        longest = 1
        count = 1

        arr.append(float('inf'))

        for i in range(1, n):
            prev,curr,next = arr[i-1], arr[i], arr[i+1]
            if prev > curr:
                count += 1
                longest = max(longest, count)
                if next <= curr:
                    count = 1
            elif prev < curr:
                count += 1
                longest = max(longest, count)
                if next >= curr:
                    count = 1
            else:
                count = 1

        return longest
