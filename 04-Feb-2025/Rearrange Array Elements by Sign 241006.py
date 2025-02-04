# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        write_pos,write_neg = 0,1

        for num in nums:
            if num < 0:
                result[write_neg] = num
                write_neg += 2
            else:
               result[write_pos] = num 
               write_pos += 2

        return result