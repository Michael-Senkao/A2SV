# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def countNodes(self, head):
        if head is None:
            return head
        tail = None
        curr = head
        count = 0
        while curr:
            count += 1
            tail = curr
            curr = curr.next

        return tail, count

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        # Count the nodes in the linked list
        tail,count = self.countNodes(head)
        k = k % count

        if not k:
            return head

        # Get the (k + 1)th node from the end
        dummy = slow = ListNode(0, head)
        fast = head
        for _ in range(k):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        
        # Update the tail pointer to point to the head
        # And set the kth node as the new head
        tail.next = head
        head = slow.next
        slow.next = None

        return head