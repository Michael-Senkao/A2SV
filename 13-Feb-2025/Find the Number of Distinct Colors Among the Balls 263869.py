# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        distinct_colors = defaultdict(int)
        colored = {}
        res = []

        for index,new_color in queries:
            prev_color = colored.get(index, 0)
            if prev_color:
                distinct_colors[prev_color] -= 1
                if distinct_colors[prev_color] == 0:
                    del distinct_colors[prev_color]
            
            distinct_colors[new_color] += 1
            colored[index] = new_color
            res.append(len(distinct_colors))
    

        return res
