# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

from collections import defaultdict, deque

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def calculateTotalImportance(self, employeeId, graph):
        total_importance = 0
        q = deque([employeeId])

        while q:
            empId = q.popleft()
            employee = graph[empId]
            total_importance += employee.importance
            for subordinate in employee.subordinates:
                q.append(subordinate)


        return total_importance
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        graph = defaultdict(Employee)
        for employee in employees:
            graph[employee.id] = employee

        return self.calculateTotalImportance(id, graph)