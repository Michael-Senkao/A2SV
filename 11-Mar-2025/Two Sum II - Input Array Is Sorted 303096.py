# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers) - 1

        while left < right:
            twoSum = numbers[left] + numbers[right]
            if twoSum < target:
                left += 1
            elif twoSum > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        return [-1, -1]