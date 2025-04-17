# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        rev1, rev2 = version1.split('.'), version2.split('.')
        n1,n2 = len(rev1), len(rev2)
       
        i = j = 0

        while i < n1 and j < n2:
            val1, val2 = int(rev1[i]), int(rev2[j])
            if val1 < val2:
                return -1
            if val2 < val1:
                return 1

            i += 1
            j += 1
        
        while i < n1:
            if int(rev1[i]):
                return 1
            i += 1
        
        while j < n2:
            if int(rev2[j]):
                return -1
            j += 1

        return 0