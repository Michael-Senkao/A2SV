# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        copy = dict()

        curr = head
        while curr:
            if curr not in copy:
                copy[curr] = Node(curr.val)
            if curr.next and curr.next not in copy:
                copy[curr.next] = Node(curr.next.val)
            if curr.random and curr.random not in copy:
                copy[curr.random] = Node(curr.random.val)

            copy[curr].next = copy.get(curr.next, None)
            copy[curr].random = copy.get(curr.random, None)
            curr = curr.next

        return copy[head]