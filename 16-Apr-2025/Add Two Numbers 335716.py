# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = tail = ListNode()
        carry = 0
        ptr1 = l1
        ptr2 = l2

        while ptr1 and ptr2:
            carry += ptr1.val + ptr2.val
            tail.next = ListNode(carry % 10)
            
            carry //= 10
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            tail = tail.next
        
        while ptr1:
            carry += ptr1.val
            tail.next = ListNode(carry % 10)
            
            tail = tail.next
            ptr1 = ptr1.next
            carry //= 10

        while ptr2:
            carry += ptr2.val
            tail.next = ListNode(carry % 10)
            
            tail = tail.next
            ptr2 = ptr2.next
            carry //= 10
            
        if carry:
            tail.next = ListNode(carry)
        return dummy.next
        