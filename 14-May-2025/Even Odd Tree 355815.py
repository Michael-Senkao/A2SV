# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.levels = []
    
    def dfs(self, node, currLevel):
        if node is None:
            return True
        if len(self.levels) == currLevel:
            if (currLevel % 2 == 0 and node.val % 2 == 0) or (currLevel % 2 == 1 and node.val % 2 == 1):
                return False
            self.levels.append(node.val)
        else:
            if currLevel % 2 == 0:
                if node.val % 2 == 0 or self.levels[currLevel] >= node.val:
                    return False
            elif node.val % 2 == 1 or self.levels[currLevel] <= node.val:
                return False

            self.levels[currLevel] = node.val
        return self.dfs(node.left, currLevel + 1) and self.dfs(node.right, currLevel + 1)


    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, 0)