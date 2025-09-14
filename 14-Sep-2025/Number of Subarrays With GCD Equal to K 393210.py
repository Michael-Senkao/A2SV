# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            return a if b == 0 else gcd(b, a%b)

        n = len(nums)
        count = 0

        for i in range(n):
            curr_gcd = 0
            for j in range(i, n):
                curr_gcd = gcd(curr_gcd, nums[j])
                count += curr_gcd == k
                if curr_gcd < k: break

        return count