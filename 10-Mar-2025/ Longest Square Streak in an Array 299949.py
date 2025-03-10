# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        longestStreak = 0
        numsSet = set(nums)

        # Iterate through all the numbers in the set
        for num in numsSet:
            # Calculate the square root of the current number
            squareRoot = int(math.sqrt(num))

            # Check if the current number is not perfect square or
            # its square is not in numsSet
            if squareRoot**2 != num or squareRoot not in numsSet:
                streak = 1 # Start a new streak
                while num**2 in numsSet:
                    streak += 1
                    num **= 2
                
                # Update the longest streak found so far
                longestStreak = max(longestStreak, streak)

        return longestStreak if longestStreak > 1 else -1

