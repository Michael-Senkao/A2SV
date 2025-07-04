# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0  # Edge case: empty grid
        
        rows, cols = len(grid), len(grid[0])
        q = deque()  # Queue for BFS to track rotten oranges
        fresh_count = 0  # Count of fresh oranges

        # Initialize queue with positions of all rotten oranges and count fresh oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        # Early exit if there are no fresh oranges to begin with
        if fresh_count == 0:
            return 0

        minute = 0  # Track elapsed time
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                # Check all 4 possible directions (up, down, left, right)
                moves = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for r, c in moves:
                    # Skip out-of-bound cells or cells that are not fresh oranges
                    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                        continue
                    # Rotten the fresh orange and add it to the queue
                    grid[r][c] = 2
                    q.append((r, c))
                    fresh_count -= 1  # Decrease fresh orange count

            # Increment time after processing one level of BFS
            minute += 1

        # If there are still fresh oranges left, return -1
        return -1 if fresh_count > 0 else minute - 1 if minute > 0 else 0