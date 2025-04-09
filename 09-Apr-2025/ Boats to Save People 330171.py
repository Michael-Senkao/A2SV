# Problem:  Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        left = 0
        right = n-1
        ans = 0
       
        people.sort()

        while left <= right:
            ans += 1
            if people[left] + people[right] <= limit:
                left+=1
    
            right -= 1
           

        return ans
