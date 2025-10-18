# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def floyd():
            for i in range(26):
                a[i][i] = 0
            for k in range(26):
                for i in range(26):
                    for j in range(26):
                        a[i][j] = min(a[i][j], a[i][k] + a[k][j])
        if len(source) != len(target):
            return -1
        a = [[float("inf") for _ in range(26)] for _ in range(26)]
        res = 0

        
        for i in range(len(original)):
            s = ord(original[i]) - ord('a')
            t = ord(changed[i]) - ord('a')
            a [s][t] = min(a[s][t], cost[i])
        
        floyd()
        # print(a[2][1])
        for i in range(len(source)):
            s = ord(source[i]) - ord('a')
            t = ord(target[i]) - ord('a')
            # print(s,t, a[s][t])
            if a[s][t] == float("inf"): return -1
            res += a[s][t]
        return res
        