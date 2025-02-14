# Problem: Largest Rectangle in Histogram (Optional) - https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [-1]
        max_area = 0

        for index in range(n):
            while stack[-1] != -1 and heights[index] <= heights[stack[-1]]:
                height = heights[stack[-1]]
                stack.pop()
                width = index - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(index)
        
        while stack[-1] != -1:
            height = heights[stack[-1]]
            stack.pop()
            width = n- stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area