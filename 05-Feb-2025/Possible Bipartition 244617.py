# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/


class Solution:
    def hasCycle(self, start,color,graph):
        q = deque([start])
        color[start] = 1
        while q:
            for _ in range(len(q)):
                person = q.popleft()
                for dislike in graph[person]:
                    if color[dislike] == color[person]:
                        return True
                    if color[dislike] == 0:
                        q.append(dislike)
                        color[dislike] = 1 if color[person] == 2 else 2

        return False
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        color = [0] * (n + 1)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(1,n+1):
            if not color[i]:
                if self.hasCycle(i, color, graph):
                    return False
     
        return True