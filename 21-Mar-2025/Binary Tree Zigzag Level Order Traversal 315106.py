# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseLeft(self, q: deque) -> List[int]:
        length = len(q)
        values = []
        for _ in range(length):
            curr = q.popleft()
            values.append(curr.val)
            
            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

        return values


    def traverseRight(self, q: deque) -> List[int]:
        length = len(q)
        values = []
        for _ in range(length):
            curr = q.pop()
            values.append(curr.val)

            if curr.right:
                q.appendleft(curr.right)

            if curr.left:
                q.appendleft(curr.left)
        return values


    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([root])
        res = []
        level = 0

        while q:
            if level % 2 == 0:
                res.append(self.traverseLeft(q))
            else:
                res.append(self.traverseRight(q))

            level += 1

        return res