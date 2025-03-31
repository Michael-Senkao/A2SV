# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, prefixSum, runningSum):
            if node is None:
                return 0
            
            runningSum += node.val
            prefixSum[runningSum] += 1
            leftCount = dfs(node.left, prefixSum, runningSum)
            rightCount = dfs(node.right, prefixSum, runningSum)
            prefixSum[runningSum] -= 1

            return leftCount + rightCount + prefixSum[runningSum - targetSum]
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        return dfs(root, prefixSum, 0)


            