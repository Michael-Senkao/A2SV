# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, num):
        if node is None:
            return 0
        
        num = num*10 + node.val
        if node.left:
            if node.right:
                return self.dfs(node.left, num) + self.dfs(node.right, num)
            return self.dfs(node.left, num)
        if node.right:
            return self.dfs(node.right, num)
        return num
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)