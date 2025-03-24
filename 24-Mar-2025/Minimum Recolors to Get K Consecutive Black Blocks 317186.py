# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        k -= 1
        whites = blocks[:k].count('W')
        res = len(blocks)
        
        for i in range(k, len(blocks)):
            whites += blocks[i] == 'W'
            res = min(res, whites)
            whites -= blocks[i - k] == 'W'

        return res