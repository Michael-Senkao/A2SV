# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def helper(self, index, cookies, k, split, unfairness):
        if index == len(cookies) or unfairness > self.res:
            return unfairness
        
        for i in range(k):
            split[i] += cookies[index]
            self.res = min(self.res, self.helper(index + 1, cookies, k, split, max(unfairness, split[i])))
            split[i] -= cookies[index]
        
        return self.res

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        split = [0] * n
        self.res = float('inf')
        return self.helper(0, cookies, k, split, 0)