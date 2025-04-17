# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        res = 0
        stack = []
        slow = fast = head
        while fast and fast.next:
            stack.append(slow.val)

            slow = slow.next
            fast = fast.next.next

        while stack and slow:
            res = max(res, stack[-1] + slow.val)
            slow = slow.next
            stack.pop()

        return res