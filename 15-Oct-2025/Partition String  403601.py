# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []
        curr = ''

        for char in s:
            curr += char
            if curr not in seen:
                seen.add(curr)
                res.append(curr)
                curr = ''
        
        if curr and curr not in seen:
            seen.add(curr)
            res.append(curr)
        return res