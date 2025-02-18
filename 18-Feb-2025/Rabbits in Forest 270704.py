# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        counter = defaultdict(int)
        for ans in answers:
            counter[ans + 1] += 1
        
        for key,val in counter.items():
            mult = val // key + (val % key != 0)
            res += (key * mult)
        return res