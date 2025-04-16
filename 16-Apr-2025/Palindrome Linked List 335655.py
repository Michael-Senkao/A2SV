# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLink(self, curr, prev):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

        return curr,prev


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        
        left = head
        right = fast = head.next
        left.next = None
        ans = True

        # Find the middle of the list 
        # Reverse the first half along the way
        while fast and fast.next:
            fast = fast.next.next
            right, left = self.reverseLink(right, left)

        # If list is odd length shift the middle one to the left
        prev = right
        if fast is None:
            left, prev = self.reverseLink(left, prev)

        # Compare the values in both halves 
        # Reverse the link along the way to get back original list
        while left:
            if left.val != right.val:
                ans = False
                break
            left, prev = self.reverseLink(left, prev)
            right = right.next
        
        # Reverse the remaining nodes to get the original list
        while left:
            left, prev = self.reverseLink(left, prev)
        
        return ans
