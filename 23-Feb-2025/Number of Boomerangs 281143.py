# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        n = len(points)
        res = 0

        for i in range(n):
            x1,y1 = points[i]
            distance_count = defaultdict(int)
            for j in range(n):
                x2, y2 = points[j]

                distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                distance_count[distance] += 1

            for dist in distance_count.values():
                res += dist * (dist - 1)

        return res