# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows,cols = len(board),len(board[0])
        directions = [(0, 1),(0, -1),(1, 0),(1, 1),(1, -1),(-1, -1),(-1, 0),(-1, 1)]

        for row in range(rows):
            for col in range(cols):
                ones = 0
                for x,y in directions:
                    dx,dy = row + x, col + y
                    if 0 <= dx < rows and 0 <= dy < cols:
                        ones += (board[dx][dy] & 1)

                if board[row][col]:
                    if ones < 2 or ones > 3:
                        board[row][col] = 3 # 1 changes to 0
                elif ones == 3:
                    board[row][col] = 2 # 0 changes to 1
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == 3:
                    board[row][col] = 0
            

        