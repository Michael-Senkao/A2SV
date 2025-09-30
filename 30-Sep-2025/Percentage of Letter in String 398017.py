# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        letter_count = 0
        for char in s:
            letter_count += (char==letter)
       
        return 100 * letter_count // len(s)