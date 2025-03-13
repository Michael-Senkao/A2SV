# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        common = 0
        res = [0]*len(A)
        freq = [0]*(len(A) + 1)

        for i in range(len(A)):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common += 1

            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common += 1
            
            res[i] = common

        return res