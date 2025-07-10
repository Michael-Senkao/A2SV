# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for indx, root in enumerate(lists):
            if root:
                heapq.heappush(min_heap, (root.val, indx))
    
        dummy = tail = ListNode()

        while min_heap:
            _, indx = heapq.heappop(min_heap)
            tail.next = lists[indx]
            tail = lists[indx]
            lists[indx] = lists[indx].next
            if lists[indx]:
                heapq.heappush(min_heap, (lists[indx].val, indx))
        return dummy.next