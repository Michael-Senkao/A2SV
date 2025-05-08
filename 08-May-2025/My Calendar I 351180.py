# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.calender = SortedList()

    def book(self, start: int, end: int) -> bool:
        if self.isOverlapping(start, end):
            return False

        self.calender.add((start, end))
        return True

    
    def isOverlapping(self, start, end):
        if not self.calender: 
            return False

        left,right = 0, len(self.calender) - 1
        while left <= right:
            mid = left + (right - left)//2
            if start >= self.calender[mid][1]:
                left = mid + 1
            elif end <= self.calender[mid][0]:
                right = mid - 1
            else:
                return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)