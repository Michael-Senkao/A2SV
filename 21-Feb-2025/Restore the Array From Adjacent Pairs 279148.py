# Problem: Restore the Array From Adjacent Pairs - https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list)
        indegree = defaultdict(int)

        for u,v in adjacentPairs:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

            indegree[u] += 1
            indegree[v] += 1

        res = []
        q = deque()

        for key,count in indegree.items():
            if count == 1:
                q.append(key)
                break


        while q:
            num = q.popleft()
            res.append(num)
            indegree[num] = 0

            for nei in adjacencyList[num]:
                if indegree[nei] != 0:
                    q.append(nei)

        return res