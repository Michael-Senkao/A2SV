# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp

        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l1 or l2

        l1_reversed = self.reverse(l1)
        l2_reversed = self.reverse(l2)

        carry = 0
        ptr1, ptr2 = l1_reversed, l2_reversed
        dummy = tail = ListNode()

        while ptr1 and ptr2:
            val = ptr1.val + ptr2.val + carry
            tail.next = ListNode(val % 10)
            tail = tail.next
            carry = val // 10
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        while ptr1:
            val = ptr1.val + carry
            tail.next = ListNode(val % 10)
            tail = tail.next
            carry = val // 10
            ptr1 = ptr1.next

        while ptr2:
            val = ptr2.val + carry
            tail.next = ListNode(val % 10)
            tail = tail.next
            carry = val // 10
            ptr2 = ptr2.next
        
        if carry:
            tail.next = ListNode(carry)
            tail = tail.next
        
        return self.reverse(dummy.next)
