# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.back = None
        self.size = 0
        self.maxSize = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = Node(value)
        if self.front is None:
            self.front = self.back = newNode
        else:
            self.back.next = newNode
            self.back = self.back.next
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = self.front.next
        self.size -= 1

        return True

    def Front(self) -> int:
        if self.front is None:
            return -1
        return self.front.val


    def Rear(self) -> int:
        if self.front is None:
            return -1
        return self.back.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxSize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()