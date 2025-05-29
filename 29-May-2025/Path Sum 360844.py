# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, currSum, targetSum):
        # Check if the current node is NULL
        if node is None:
            return False

        currSum += node.val
        # Check if the current node is a ROOT node
        if not node.left and not node.right:
            return currSum == targetSum
        return self.traverse(node.left, currSum, targetSum) or self.traverse(node.right, currSum, targetSum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        return self.traverse(root, 0, targetSum)