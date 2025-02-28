# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_row , max_count = 0,0

        for row,arr in enumerate(mat):
            count = sum(arr)
            if count > max_count:
                max_row = row
                max_count = count

        return [max_row, max_count]