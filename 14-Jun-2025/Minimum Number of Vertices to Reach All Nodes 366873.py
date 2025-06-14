# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        can_not_reach = set(range(n))
        for u,v in edges:
            if v in can_not_reach:
                can_not_reach.remove(v)

        return list(can_not_reach)