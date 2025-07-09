# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3 or arr[1] < arr[0]:
            return False
        
        for i in range(1, n):
            if arr[i] <= arr[i-1]:
                break
        for j in range(i, n):
            if arr[j] >= arr[j - 1]:
                return False
        return True