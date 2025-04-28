# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(list(range(len(tickets))))
        totalTime = 0
        while queue:
            totalTime += 1
            index = queue.popleft()
            tickets[index] -= 1
            if tickets[index] == 0:
                if index == k:
                    return totalTime
            else:
                queue.append(index)


        return totalTime
        