# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def countDays(self, maxCapacity, weights):
        currCapacity = 0
        days = 1
        for weight in weights:
            currCapacity += weight
            if currCapacity > maxCapacity:
                days += 1
                currCapacity = weight
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        left,right = max(weights), sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if self.countDays(mid, weights) > days:
                left = mid + 1
            else:
                right = mid
                
        return left