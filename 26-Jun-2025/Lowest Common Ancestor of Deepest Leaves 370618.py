# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node is None:
            return node, 0
        leftLCA, leftD = self.dfs(node.left)
        rightLCA, rightD = self.dfs(node.right)
        if leftD == rightD:
            return node, leftD + 1
        if leftD > rightD:
            return leftLCA, leftD + 1
        return rightLCA, rightD + 1
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)[0]