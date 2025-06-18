# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, currNode, nodes, sum, targetSum, res):
        if currNode is None:
            return
        sum += currNode.val
        nodes.append(currNode.val)
        if currNode.left:
            self.dfs(currNode.left, nodes, sum, targetSum, res)
            if currNode.right:
                self.dfs(currNode.right, nodes, sum, targetSum, res)
        elif currNode.right:
            self.dfs(currNode.right, nodes, sum, targetSum, res)
        elif sum == targetSum:
            res.append(nodes[:])
        nodes.pop()
            

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        self.dfs(root, [], 0, targetSum, res)
        return res