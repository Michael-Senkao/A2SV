# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def pow(self, base, exponent, MOD):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        half = (self.pow(base, exponent // 2, MOD)) % MOD
        full = (half * half) % MOD
        if exponent & 1:
            full = (full * base) % MOD
        return full

    def countGoodNumbers(self, n: int) -> int:
        MOD = 1_000_000_007

        odd = n // 2
        even = n - odd

        return (self.pow(5, even, MOD) * self.pow(4, odd, MOD)) % MOD
        