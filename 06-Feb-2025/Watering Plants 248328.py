# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        curr_capacity = capacity
        
        steps = 1

        for i in range(n-1):
            curr_capacity -= plants[i]
            if plants[i + 1] > curr_capacity:
                curr_capacity = capacity
                steps += (i + 1)*2
            steps += 1

        return steps