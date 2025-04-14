# Problem: Insert a Node at the Tail of a Linked List - https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

def insertNodeAtTail(head, data):
    dummy = tail = SinglyLinkedListNode(0)
    dummy.next = head
    while tail.next is not None:
        tail = tail.next
    tail.next = SinglyLinkedListNode(data)
    return dummy.next