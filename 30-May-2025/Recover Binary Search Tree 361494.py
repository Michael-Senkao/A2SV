# Problem: Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraverse(self, node, values):
        if node:
            self.inorderTraverse(node.left, values)
            values.append(node.val)
            self.inorderTraverse(node.right, values)
    def sort(self, values):
        maxInd = minInd = -1

        for i in range(1, len(values)):
            if values[i] < values[i-1]:
                if minInd < 0:
                    minInd, maxInd = i, i - 1
                else:
                    minInd = i
        values[minInd], values[maxInd] = values[maxInd], values[minInd]


    def createTree(self, node, values):
        if node:
            self.createTree(node.left, values)
            node.val = values.popleft()
            self.createTree(node.right, values)
            
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        values = deque()
        self.inorderTraverse(root, values)
        
        self.sort(values)
        self.createTree(root, values)
       
        