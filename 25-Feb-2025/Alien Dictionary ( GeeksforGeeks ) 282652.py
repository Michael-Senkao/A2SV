# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

class Solution:
    
    def findOrder(words):
        res = []  
        found = [False] * 26  
        stack = [False] * 26
        visited = [False] * 26  
        adj_matrix = [[0 for _ in range(26)] for _ in range(26)]
        isCycle = False


        def dfs(u):
            nonlocal isCycle 
            visited[u] = stack[u] = True
            for v in range(26):
                if adj_matrix[u][v] and not visited[v]:
                    dfs(v)
                elif adj_matrix[u][v] and stack[v]:
                    isCycle  = True
            res.append(chr(ord('a') + u))
            stack[u] = False

        for word in words:
            for ch in word:
                found[ord(ch) - ord('a')] = True

    
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            n, m, ind = len(first), len(second), 0
            while ind < n and ind < m and first[ind] == second[ind]:
                ind += 1
            if ind != n and ind == m:
                return ""
            if ind < n and ind < m:
                adj_matrix[ord(first[ind]) - ord('a')][ord(second[ind]) - ord('a')] = 1

        for i in range(26):
            if found[i] and not visited[i]:
                dfs(i)

        if isCycle:
            return ""
        res.reverse()
        return "".join(res)