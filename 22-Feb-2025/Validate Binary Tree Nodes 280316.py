# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0]*n
        q = deque()
        visited = [0]*n

        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]

            if left > -1:
                if indegree[left]:
                    return False
                indegree[left] = 1
            if right > -1:
                if indegree[right]:
                    return False
                indegree[right] = 1
        
        for i in range(n):
            if not indegree[i]:
                q.append(i)
                break

        if q:
            visited[q[0]] = 1
        while q:
            node = q.popleft()
            left = leftChild[node]
            right = rightChild[node]

            if left > -1 and not visited[left]:
                q.append(left)
                visited[left] = 1
            if right > -1 and not visited[right]:
                q.append(right)
                visited[right] = 1

        return sum(visited) == n
