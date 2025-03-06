# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols = len(image),len(image[0])
        startColor = image[sr][sc]
        if startColor == color:
            return image
        q = deque([(sr,sc)])

        while q:
            row,col = q.popleft()
            image[row][col] = color

            if row > 0 and image[row - 1][col] == startColor:
                q.append((row - 1, col))
            if col > 0 and image[row][col - 1] == startColor:
                q.append((row, col - 1))
            if row + 1 < rows and image[row + 1][col] == startColor:
                q.append((row + 1, col))
            if col + 1 < cols and image[row][col + 1] == startColor:
                q.append((row, col + 1))

        return image