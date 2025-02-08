# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()

        for num in nums:
            if num in seen_set: 
                return True
            seen_set.add(num)

        return False