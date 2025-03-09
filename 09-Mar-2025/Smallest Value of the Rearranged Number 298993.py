# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        zeros = 0
        
        digits = []
        temp = num if num >= 0 else -num
        while temp:
            digit = temp % 10
            if digit:
                digits.append(str(digit))
            else:
                zeros += 1
            temp //= 10

        digits.sort(reverse=True)

        if num < 0:
            
            digits.extend('0'*zeros)
            res = ''.join(digits)

            return -int(res)

        first = digits.pop()
        digits.extend('0'*zeros)
        digits.append(first)

        res = ''.join(digits[-1::-1])
        return int(res)
        