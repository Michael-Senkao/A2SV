# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        found = set()
        count = 1

        for char in s:
            if char in found:
                count += 1
                found.clear()
            found.add(char)

        return count