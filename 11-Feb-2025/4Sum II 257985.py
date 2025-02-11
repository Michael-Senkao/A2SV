# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        two_sum = defaultdict(int)
        res = 0

        for i in range(n):
            for j in range(n):
                _sum = nums1[i] + nums2[j]
                two_sum[_sum] += 1

        for k in range(n):
            for l in range(n):
                need = -(nums3[k] + nums4[l])
                res += two_sum.get(need, 0)

        return res
                