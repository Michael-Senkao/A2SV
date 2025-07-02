# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def createGraph(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                createGraph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                createGraph(node.right)

        graph = defaultdict(list)
        result = []
        createGraph(root)

        q = deque([target.val])
        visited = set()
        visited.add(target.val)

        while k > 0 and q:
            k -= 1
            for _ in range(len(q)):
                node = q.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)

        # print(q)
        return list(q)