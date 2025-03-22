# Problem: Cousins in Binary Tree II - https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prev_level_sum = root.val
        q = deque()
        q.append(root)

        # Update the tree values
        while q:
            level_sum = 0
            for _ in range(len(q)):
                curr_node = q.popleft()
                curr_node.val = prev_level_sum - curr_node.val

                if curr_node.left:
                    level_sum += curr_node.left.val
                    if curr_node.right:
                        level_sum += curr_node.right.val
                        curr_node.left.val += curr_node.right.val
                        curr_node.right.val = curr_node.left.val
                        q.append(curr_node.right)

                    q.append(curr_node.left)
                elif curr_node.right:
                    level_sum += curr_node.right.val
                    q.append(curr_node.right)
            
            prev_level_sum = level_sum
            
        return root