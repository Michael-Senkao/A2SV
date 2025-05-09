# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        # Helper to compute a^k % MOD
        def power(x, k):
            res = 1
            x %= MOD
            for _ in range(k):
                res = (res * x) % MOD
            return res

        if not b:
            return 1

        last_digit = b.pop()
        part1 = power(self.superPow(a, b), 10)
        part2 = power(a, last_digit)

        return (part1 * part2) % MOD
            