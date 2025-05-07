# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # Left half is sorted
                # Check if target lies in the left half
                if nums[left] <= target <= nums[mid]: 
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= target <= nums[right]: # Check if target lies in the right half
                left = mid + 1
            else:
                right = mid - 1

        return -1