# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        indegree = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        prerequisites_dict = defaultdict(set)

        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            for nei in graph[curr]:
                prerequisites_dict[nei].add(curr)
                prerequisites_dict[nei].update(prerequisites_dict[curr])
    
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        res = [u in prerequisites_dict[v] for u,v in queries]
      
        return res
                        