# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        
        for num in {2,3,5}:
            while n > 1 and n % num == 0:
                n //= num

        return n == 1