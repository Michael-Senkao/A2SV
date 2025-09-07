# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        result = ['-1'] * n
        score_to_index = list(enumerate(score))
        score_to_index.sort(key=lambda x: x[1], reverse=True)
        
        if n > 0:
            result[score_to_index[0][0]] = "Gold Medal"
        if n > 1:
            result[score_to_index[1][0]] = "Silver Medal"
        if n > 2:
            result[score_to_index[2][0]] = "Bronze Medal"

        for i in range(4, n + 1):
            index, _ = score_to_index[i - 1]
            result[index] = str(i)
        return result