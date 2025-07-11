# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        is_negative = num < 0

        if is_negative:
            num = -num

        zero_count = 0
        digits = []
        while num > 0:
            digit = num % 10
            if digit:
                digits.append(str(digit))
            else:
                zero_count += 1
            num //= 10
        
        if not digits:
            return 0
        digits.sort()
        digits = ''.join(digits)
        res_str = ''
        if is_negative:
            res_str = digits[-1: : -1] + '0' * zero_count
        else:
            res_str = digits[0] + '0' * zero_count + digits[1:]
        
        return -int(res_str) if is_negative else int(res_str)
