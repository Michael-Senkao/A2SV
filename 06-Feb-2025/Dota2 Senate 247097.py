# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_queue = deque()
        d_queue = deque()

        for i in range(n):
            if senate[i] == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
        
        while r_queue and d_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()
            if r < d:
                r_queue.append(r + n)
            else:
                d_queue.append(d + n)
        
        return "Radiant" if r_queue else "Dire"
