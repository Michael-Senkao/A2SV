# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/


from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        graph = defaultdict(list)
        indegree = [0] * numCourses
        taken = 0

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        while q:
            c = q.popleft()
            res.append(c)
            taken += 1
            for nei in graph[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res if taken == numCourses else []