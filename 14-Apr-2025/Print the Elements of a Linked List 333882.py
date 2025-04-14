# Problem: Print the Elements of a Linked List - https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

def printLinkedList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.next
