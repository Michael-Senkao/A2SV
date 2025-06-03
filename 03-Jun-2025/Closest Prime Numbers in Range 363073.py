# Problem: Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right < 3:
            return [-1, -1]

        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        num1 = num2 = -1
        prev = -1

        for i in range(2, right + 1):
            if is_prime[i]:
                if prev >= left and (num1 < 0 or i - prev < num2 - num1):
                    num1, num2 = prev, i
                prev = i
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False
        
        return [num1, num2]