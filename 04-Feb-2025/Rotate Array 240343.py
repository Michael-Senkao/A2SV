# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        
        n = len(nums)
        k %= n
        if k == 0:
            return
            
        swaps = 0
        for i in range(n):
            if swaps >= n:
                return
            swap_index = (i + k) % n
            while swaps < n and swap_index != i:
                nums[i],nums[swap_index] = nums[swap_index],nums[i]
                swap_index = (swap_index + k) % n
                swaps += 1
            swaps += 1
        