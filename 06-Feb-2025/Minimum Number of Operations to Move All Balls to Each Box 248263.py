# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        moves = []
        left_balls,right_balls = 0,0

        prev_moves = 0
        # Move left balls to i
        for i in range(n):
            moves.append(prev_moves + left_balls)
            if boxes[i] == '1':
                left_balls += 1
            prev_moves = moves[i]

        prev_moves = 0
        # Move right balls to i
        for i in range(n - 1, -1, -1):
            right_moves = prev_moves + right_balls
            moves[i] += right_moves
            if boxes[i] == '1':
                right_balls += 1
            prev_moves = right_moves

        return moves
            