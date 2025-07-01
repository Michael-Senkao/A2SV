# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorderSum = 0

    def inorderTraverse(self, node):
        if node is None:
            return
        self.inorderTraverse(node.right)
        self.inorderSum += node.val
        node.val = self.inorderSum
        self.inorderTraverse(node.left)
        
        
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inorderTraverse(root)
        return root