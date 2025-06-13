# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    
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

        digits_to_letters = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", 
        "7":"pqrs", "8": "tuv", "9":"wxyz"
        }
        res = []
        
        self.generateCombinations(0, digits, digits_to_letters, [], res)
        return res
        
