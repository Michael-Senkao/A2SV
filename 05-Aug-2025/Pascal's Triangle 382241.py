# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
   
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for _ in range(numRows - 1):
            currRow = [1]
            prevRow = res[-1]
            for i in range(1, len(prevRow)):
                currRow.append(prevRow[i] + prevRow[i-1])
            currRow.append(1)
            res.append(currRow)
        return res