# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nextGreater = [-1]*n
        stack = []

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                elementIndex = stack.pop()
                nextGreater[elementIndex] = nums[i]
            stack.append(i)
        
        nextGreaterIndex = 0
        while stack and nextGreaterIndex < stack[-1]:
            if nums[stack[-1]] < nums[nextGreaterIndex]:
                elementIndex = stack.pop()
                nextGreater[elementIndex] = nums[nextGreaterIndex]
            else:
                nextGreaterIndex += 1

        return nextGreater