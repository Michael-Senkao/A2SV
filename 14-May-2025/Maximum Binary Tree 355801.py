# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, left, right, nums, indices):
        if left >= right:
            return None

        max_value = max(nums[left:right])
        index = indices[max_value]

        newNode = TreeNode(max_value)
        newNode.left = self.helper(left, index, nums, indices)
        newNode.right = self.helper(index + 1, right, nums, indices)

        return newNode


    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # Map each value to its index
        indices = {num:index for index,num in enumerate(nums)}
        
        return self.helper(0, len(nums), nums, indices)