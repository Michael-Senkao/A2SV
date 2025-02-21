# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        count = defaultdict(int)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                count[nums[i] * nums[j]] += 1

        for val in count.values():
            res += ((val - 1) * val // 2)*8
        return res