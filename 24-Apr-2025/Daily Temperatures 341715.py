# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for index,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                poppedIndex = stack.pop()
                ans[poppedIndex] = index - poppedIndex
            stack.append(index)

        return ans