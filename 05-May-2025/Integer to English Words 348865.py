# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def __init__(self):
        self.digitsWord = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
        }
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        digits = list(reversed(str(num)))
        res = []
        positions = ['Hundred', 'Thousand', 'Million', 'Billion']
        
        padding = 3 - (len(digits) % 3)
        if padding < 3:
            digits.extend(['0']*padding)
       
        for pos in range(len(digits) // 3):
            start = pos*3
            first,second,third = digits[start: start + 3]
            if first == second == third == '0':
                continue

            prefix = int(second + first)
            if pos > 0:
                res.append(positions[pos])
            
            if  prefix > 0 and (prefix < 20 or first == '0'):
                res.append(self.digitsWord[prefix])
            elif prefix > 0:
                res.extend([self.digitsWord[int(first)], self.digitsWord[int(second)*10]])
            if third != '0':
                res.extend(['Hundred', self.digitsWord[int(third)]])
    
                
        return ' '.join(reversed(res))