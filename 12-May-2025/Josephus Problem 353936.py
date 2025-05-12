# Problem: Josephus Problem - https://www.geeksforgeeks.org/josephus-problem/

class Solution:
    def josephus(self,n,k):
        #Your code here
        def helper(n,k):
            if n == 1:
                return 0
            return ((helper(n - 1, k) + k) % n)
        return helper(n,k) + 1
