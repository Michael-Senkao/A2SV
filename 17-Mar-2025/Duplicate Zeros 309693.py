# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        n = len(arr)

        for i in range(n - 2, -1,- 1):
            if arr[i] == 0:
                j = n - 2
                while j > i:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = 0
        