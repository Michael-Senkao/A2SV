# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        indegree = [0] * numCourses
        graph = defaultdict(list)
        visited_count = 0

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                visited_count += 1

        while q:
            node = q.popleft()
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    visited_count += 1
        
        return visited_count == numCourses