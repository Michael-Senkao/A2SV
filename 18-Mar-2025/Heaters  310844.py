# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n,m = len(houses), len(heaters)
        houses.sort()
        heaters.sort()
        minRadius = float("-inf")

        i,j = 0,0

        while i < n:
            while j < m and heaters[j] <= houses[i]:
                j += 1

            if j > 0:
                if j < m:
                    minRadius = max(minRadius, min(houses[i] - heaters[j-1], heaters[j] - houses[i]))
                else:
                    minRadius = max(minRadius, houses[i] - heaters[j-1])
            else:
                minRadius = max(minRadius, heaters[j] - houses[i])

            i += 1

        return minRadius
