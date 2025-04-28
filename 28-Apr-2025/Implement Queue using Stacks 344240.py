# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack2.append(x)
        if len(self.stack2) - len(self.stack1) > 1:
            self.reorder()

    def pop(self) -> int:
        if not self.stack1 and not self.stack2:
            return -1
        if not self.stack1:
            return self.stack2.pop()
        val = self.stack1.pop()
        if len(self.stack2) - len(self.stack1) > 1:
            self.reorder()
        return val

    def peek(self) -> int:
        if not self.stack1 and not self.stack2:
            return -1
        if not self.stack1:
            return self.stack2[-1]
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def reorder(self):
        temp = []
        while self.stack2:
            temp.append(self.stack2.pop())
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(temp.pop())
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        while temp:
            self.stack2.append(temp.pop())
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()