# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefixSum = [0] * (n + 1)
        for start, end, direction in shifts:
            if direction:
                prefixSum[start]+=1
                prefixSum[end+1]-=1
            else:
                prefixSum[start]-=1
                prefixSum[end+1]+=1


        
        s = list(s)

        total_shifts = ((ord(s[0]) - 97) + prefixSum[0] ) % 26
        s[0] = chr(total_shifts + 97)
        
        for i in range( 1, n):
            prefixSum[i] = (prefixSum [i] + prefixSum[i-1]) % 26
            if prefixSum[i] < 0:
                prefixSum[i] += 26

            total_shifts = ((ord(s[i]) - 97) + prefixSum[i] ) % 26
            s[i] = chr(total_shifts + 97)
        return ''.join(s)