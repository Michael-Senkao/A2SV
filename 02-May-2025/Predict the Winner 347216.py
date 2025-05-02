# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def backtrack(left, right, p1_turn):
            if left > right:
                return 0,0
            p1_left,p2_left = backtrack(left + 1, right, not p1_turn)
            p1_right,p2_right = backtrack(left, right - 1, not p1_turn)

            if p1_turn:
                p1_left += nums[left] 
                p1_right += nums[right]

                if p1_left > p1_right:
                    return p1_left, p2_left
                return p1_right, p2_right

            else:
                p2_left += nums[left] 
                p2_right += nums[right]

                if p2_left > p2_right:
                    return p1_left, p2_left
                return p1_right, p2_right

        p1_score, p2_score = backtrack(0, len(nums) - 1, True)
        return p1_score >= p2_score
