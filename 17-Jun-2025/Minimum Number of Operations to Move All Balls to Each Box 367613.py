# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = []

        count = 0
        cost = 0
        for box in boxes:
            cost += count
            res.append(cost)
            count += box == '1'

        count = 0
        cost = 0
        for i in range(n-1, -1, -1):
            cost += count
            res[i] += cost
            count += boxes[i] == '1'
    
        return res