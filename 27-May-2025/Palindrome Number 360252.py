# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        x_str = str(x)
        i,j = 0, len(x_str) - 1

        while i < j:
            if x_str[i] != x_str[j]:
                return False
            i += 1
            j -= 1
        return True