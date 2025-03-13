# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        firstKIndex = 0

        for num in nums:
            if num != val:
                nums[firstKIndex] = num
                firstKIndex += 1

        return firstKIndex