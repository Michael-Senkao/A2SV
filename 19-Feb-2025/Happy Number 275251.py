# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def sumOfDigits(self, n):
        sum_of_digits_square = 0
        while n > 0:
            digit = n % 10
            sum_of_digits_square += (digit**2)
            n //= 10

        return sum_of_digits_square

    def isHappy(self, n: int) -> bool:
        found = {}
        while True:
            n = self.sumOfDigits(n)
            if n == 1:
                return True
            elif n in found:
                return found[n]
            found[n] = False

        return False
        