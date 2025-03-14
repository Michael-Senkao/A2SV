# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        left,right = 0, len(nums) - 1
        pairs = 0

        while left < right:
            if nums[left] + nums[right] >= target:
                right -= 1
            else:
                pairs += right - left
                left += 1

        return pairs