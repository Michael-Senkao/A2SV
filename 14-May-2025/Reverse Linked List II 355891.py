# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = tail = ListNode(0, head)
        curr = head
        start = None

        for _ in range(1, left):
            tail = tail.next
            curr = curr.next
        
        end = curr
        tail.next = None
        prev = None

        for _ in range(left, right + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        tail.next = prev
        end.next = curr
        return dummy.next

        