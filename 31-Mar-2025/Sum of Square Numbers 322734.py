# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))

        while left <= right:
            sum_of_sqr = left*left + right*right
            if sum_of_sqr < c:
                left += 1
            elif sum_of_sqr > c:
                right -= 1
            else:
                return True

        return False
        