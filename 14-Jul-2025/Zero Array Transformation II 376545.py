# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        n = len(nums)
        if nums.count(0) == n:
            return 0
        prefix = [0] * n

        for left,right,value in queries:
            prefix[left] += value
            if right + 1 < n:
                prefix[right + 1] -= value

        if prefix[0] < nums[0]:
            return -1

        for i in range(1, n):
            prefix[i] += prefix[i - 1]
            if prefix[i] < nums[i]:
                return -1

        i = len(queries) - 1
        while i >= 0:
            left,right,val = queries[i]
            for j in range(left, right + 1):
                prefix[j] -= val
                if prefix[j] < nums[j] :
                    return i + 1

            i -= 1
        return i + 1