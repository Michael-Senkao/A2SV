# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = tail = ListNode()
        curr = head

        while curr and curr.next:
            tail.next = curr.next
    
            temp = curr.next.next
            curr.next.next = curr
            curr.next = temp
            curr = temp
            tail = tail.next.next
        return dummy.next