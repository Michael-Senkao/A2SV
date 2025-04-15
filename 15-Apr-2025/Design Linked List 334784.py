# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
            
        idx = 0
        curr = self.head
        while curr and idx < index:
            curr = curr.next
            idx += 1
            
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        self.size += 1
        
        if not self.head:
            self.head = self.tail = Node(val) 
            return 
            
        newNode = Node(val, self.head)
        self.head = newNode 
               

    def addAtTail(self, val: int) -> None:
    
        newNode = Node(val)
        if self.head is None:
            self.head = self.tail = newNode
        else:  
            self.tail.next = newNode
            self.tail = newNode
            
        self.size += 1   
            
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
            
        if index == self.size:
            self.addAtTail(val)
            return 
            
        
        if index == 0:
            self.addAtHead(val)
            return
        else:
            newNode = Node(val)
            ptr = self.head
            for _ in range(0, index - 1):
                ptr = ptr.next
                
            newNode.next = ptr.next
            ptr.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0 or self.head is None:
            return
        
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None  
        else:
            ptr = self.head
            for _ in range(0, index - 1):
                ptr = ptr.next
            
            if ptr.next == self.tail:
                self.tail = ptr
                
            ptr.next = ptr.next.next
            
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)