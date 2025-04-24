# Problem: Flatten a Multilevel Doubly Linked List - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def __init__(self):
        self.dummy = self.tail = Node(0, None, None, None)

    def traverse(self, node):
        if node is None:
            return

        child = node.child
        next = node.next
        node.child = node.next= None
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
    
        self.traverse(child)
        self.traverse(next)


    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
       
        self.traverse(head)
        self.tail.next = None
        newHead = self.dummy.next
        newHead.prev = None
        self.dummy.next = None
        return newHead

