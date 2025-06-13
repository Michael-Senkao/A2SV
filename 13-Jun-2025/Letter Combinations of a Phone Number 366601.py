# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def mapDigits(self):
        digits_to_letters = dict()
        curr_char = ord('a')
        for digit in range(2, 10):
            letters = []
            count = 4 if digit == 7 or digit == 9 else 3
            for _ in range(count):
                letters.append(chr(curr_char))
                curr_char += 1
            digits_to_letters[str(digit)] = letters

        return digits_to_letters


    def generateCombinations(self, index, digits, digits_to_letters, curr_str, res):
        if index == len(digits):
            res.append(''.join(curr_str))
            return

        for letter in digits_to_letters[digits[index]]:
            curr_str.append(letter)
            self.generateCombinations(index + 1, digits, digits_to_letters, curr_str, res)
            curr_str.pop()


    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        digits_to_letters = self.mapDigits()
        res = []
        
        self.generateCombinations(0, digits, digits_to_letters, [], res)
        return res
        
