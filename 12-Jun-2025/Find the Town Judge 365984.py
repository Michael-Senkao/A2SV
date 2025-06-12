# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
      
        trust_count = [[0,0] for _ in range(n)] # [trusts, trusted by]

        for u,v in trust:
            trust_count[v - 1][1] += 1
            trust_count[u - 1][0] += 1

        for idx,(trusts,trusted_by) in enumerate(trust_count):
            if trusts == 0 and trusted_by == n - 1:
                return idx + 1
        return -1