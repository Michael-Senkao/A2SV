# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        if not mat or not mat[0]:
            return []
        
        rows,cols = len(mat), len(mat[0])
        diagonals_elements = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                diagonals_elements[r+c].append(mat[r][c])

        res = []
        for key in range(rows + cols - 1):
            
            values = diagonals_elements[key]
            if key % 2 == 0:
                res.extend(reversed(values))
            else:
                res.extend(values)
        
        return res

        