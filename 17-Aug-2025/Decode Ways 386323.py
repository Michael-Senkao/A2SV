# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(index, prev):
            if prev[0] == '0':
                return 0
            if index == len(s):
                return 1
            
            if (index, prev) in memo:
                return memo[(index, prev)]
            x = dp(index + 1, s[index])
            if int(prev + s[index]) <= 26:
                x += dp(index + 1, prev + s[index])
            memo[(index, prev)] = x
            return memo[(index, prev)]

        
        return(dp(1, s[0]))