# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        onesRight = sum(nums)
        zerosLeft = 0
        maxScore = 0

        res = []
        for i in range(n):
            score = zerosLeft + onesRight
            
            if score > maxScore:
                res = [i]
                maxScore = score
            elif score == maxScore:
                res.append(i)
            
            if nums[i]:
                onesRight -= 1
            else:
                zerosLeft += 1

        if maxScore == zerosLeft:
            res.append(n)
        elif zerosLeft > maxScore:
            res = [n]
        return res
