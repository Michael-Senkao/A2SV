# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_mod = 0
        res = 0
        remainders = defaultdict(int)
        remainders[0] = 1

        for i in range(0, n):
            prefix_mod = (prefix_mod + nums[i]) % k
           
            res += remainders[prefix_mod]
            remainders[prefix_mod] += 1

        return res
