# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = dict()
        stack = []
        res = []

        for num in nums2:
            while stack and num > stack[-1]:
                nextGreater[stack[-1]] = num
                stack.pop()
            stack.append(num)

        for num in nums1:
            res.append(nextGreater.get(num, -1))

        return res