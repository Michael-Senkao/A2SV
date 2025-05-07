# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(arr)
        multiples = [1] * n
        stack = []
        res = 0

        # Compute the total number of time each value in arr will be the minimum and store it in 'multiples'
        for index, val in enumerate(arr):
            while stack and arr[stack[-1]] >= val:
                indx = stack.pop()
                multiples[indx] *= (index - indx)
            if not stack:
                multiples[index] = index + 1
            else:
                multiples[index] = index - stack[-1]
                
            stack.append(index)

        # Compute the multiples for the rest of the indices in the stack
        while stack:
            indx = stack.pop()
            multiples[indx] *= (n - indx)

        # Calculate the result
        for i in range(n):
            # Multiply each value in arr by the total number of times it would be the minimum
            res = (res + ((arr[i] * multiples[i]) % MOD)) % MOD

        return res