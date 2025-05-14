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

        # Find the tail of the list up to left - 1
        for _ in range(1, left):
            tail = tail.next
            curr = curr.next
        
        end = curr
        tail.next = None
        prev = None

        # Reverse the remaining list up to position 'right'
        for _ in range(left, right + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # Append the reversed list to the lists that are before and after it
        tail.next = prev
        end.next = curr
        return dummy.next

        