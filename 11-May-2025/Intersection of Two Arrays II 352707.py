# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1,n2 = len(nums1), len(nums2)
        nums1_freq = defaultdict(int)
        res = []

        if n1 > n2:
            nums1,nums2 = nums2,nums1

        for num in nums1:
            nums1_freq[num] += 1

        for num in nums2:
            if nums1_freq[num] > 0:
                res.append(num)
                nums1_freq[num] -= 1

        return res
        