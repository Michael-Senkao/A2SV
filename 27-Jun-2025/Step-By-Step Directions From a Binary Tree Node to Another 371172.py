# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, side, startValue, destValue):
        if node is None:
            return 0, ''
        left, pathL = self.dfs(node.left, 'L', startValue, destValue)
        right, pathR = self.dfs(node.right, 'R', startValue, destValue)

        if right == 3:
            return right, pathR
        if left == 3:
            return left, pathL

        if left == 1:
            if node.val == destValue:
                return 3, pathL
            if right:
                return 3, pathL + pathR
            return 1, pathL + 'U'
        if left == 2:
            if node.val == startValue:
                return 3, pathL
            if right:
                return 3, pathR + pathL
            return 2, side + pathL
        if right == 1:
            if node.val == destValue:
                return 3, pathR
            return 1, pathR + 'U'
        if right == 2:
            if node.val == startValue:
                return 3, pathR
            return 2, side + pathR
        
        if node.val == startValue:
            return 1, 'U'
        if node.val == destValue:
            return 2, side
        return 0, ''

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        return self.dfs(root, '', startValue, destValue)[-1]