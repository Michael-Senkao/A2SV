# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def countNodes(self, head):
        ptr = head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next

        return count


    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.countNodes(head)
        partSize = n // k
        extra = n % k
        res = []

        curr = head
        for i in range(k):
            dummy = tail = ListNode()
            for _ in range(partSize):
                tail.next = curr
                curr = curr.next
                tail = tail.next
            if extra:
                tail.next = curr
                curr = curr.next
                tail = tail.next
                extra -= 1
            tail.next = None
            res.append(dummy.next)

        return res

        