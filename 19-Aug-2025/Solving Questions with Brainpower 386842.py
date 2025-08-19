# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = [-1] * n

        def dp(index, questions, memo):
            if index >= len(questions):
                return 0

            if memo[index] != -1:
                return memo[index]

            take = questions[index][0] + dp(index + questions[index][1] + 1, questions, memo)
            skip = dp(index + 1, questions, memo)

            memo[index] = max(take, skip)
            return memo[index]

        return dp(0, questions, memo)