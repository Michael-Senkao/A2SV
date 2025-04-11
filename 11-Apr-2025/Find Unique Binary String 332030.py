# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def invert(self, char):
        return '0' if char == '1' else '1'

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = [None] * len(nums)

        for index, num in enumerate(nums):
            res[index] = self.invert(num[index])

        return ''.join(res)