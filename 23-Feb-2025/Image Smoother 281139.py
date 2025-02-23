# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def calculateAvg(self, x, y, img):
        rows,cols = len(img), len(img[0])
        _sum,count = img[x][y],1

        directions = [(0,1), (0,-1), (1,0), (-1, 0), (-1,-1), (-1,1),(1,1),(1,-1)]

        for dx,dy in directions:
            if (0 <= (x + dx) < len(img)) and (0 <= (y + dy) < len(img[0])):
                count += 1
                _sum += img[x + dx][y + dy]

        return _sum // count



    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if not img:
            return []
        rows,cols = len(img), len(img[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                res[row][col] = self.calculateAvg(row, col, img)

        return res