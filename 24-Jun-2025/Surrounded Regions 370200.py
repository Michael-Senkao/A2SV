# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def dfs(self, r, c, board):
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'O':
            board[r][c] = 'Z' # Mark it is not captured
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for x,y in directions:
                self.dfs(r + x, c + y, board)


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols = len(board), len(board[0])
        # Do not capture the 'O's on the FIRST ROW
        for c in range(cols):
            self.dfs(0, c, board)

        # Do not capture the 'O's on the LAST ROW
        for c in range(cols):
            self.dfs(rows - 1, c, board)

        # Do not capture the 'O's on the FIRST COLUMN
        for r in range(rows):
            self.dfs(r, 0, board)

        # Do not capture the 'O's on the LAST COLUMN
        for r in range(rows):
            self.dfs(r, cols - 1, board)

        for r in range(rows):
            for c in range(cols):
                char = board[r][c]
                board[r][c] = 'O' if char == 'Z' else 'X'
