# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.maxSize = k
        self.queue = [0] * k
        self.front = self.back = -1

    def enQueue(self, value: int) -> bool:
        if self.size == self.maxSize:
            return False
        if self.size == 0:
            self.front += 1

        self.back = (self.back + 1) % self.maxSize
        self.queue[self.back] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
       
        self.front = (self.front + 1) % self.maxSize
        self.size -= 1
        if self.size == 0:
            self.front = self.back = -1
        return True

    def Front(self) -> int:
        return self.queue[self.front] if self.size else -1

    def Rear(self) -> int:
        return self.queue[self.back] if self.size else -1

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