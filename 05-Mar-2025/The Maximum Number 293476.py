# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-infinity')

        for num in nums:
            # Check if num is equal to either first,second, or third
            if num in {first, second, third}:
                continue

            if num > first:
                # Current num is greater than first
                third = second
                second = first
                first = num
            elif num > second:
                # Current num is greater than second
                third = second
                second = num
            elif num > third:
                # Current num is greater than third
                third = num
   
        return third if third != float('-infinity') else first