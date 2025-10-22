# Problem: Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode(-101)
        curr = head
        while curr:
            node = curr
            curr = curr.next
            if curr and curr.val == node.val:
                while curr and curr.val == node.val:
                    curr = curr.next
            else:
                tail.next = node
                tail = tail.next
        tail.next = None
        return dummy.next