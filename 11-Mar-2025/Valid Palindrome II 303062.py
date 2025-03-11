# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right = 0,len(s) - 1
        hasDeleted = False

        while left < right:
            if s[left] != s[right]:
                break

            left += 1
            right -= 1

        
        if left >= right:
            return True # String is already a palindrome

        # Try moving the left deviating character
        l,r = left + 1,right
        while l < r:
            if s[l] != s[r]:
                break
            l += 1
            r -= 1

        if l >= r:
            return True
        
        # Try moving the right deviating character
        l,r = left,right - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
