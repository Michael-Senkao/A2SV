# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""

        # thousands
        thousands = num//1000
        num %= 1000
        while thousands > 0:
            ans += "M"
            thousands -= 1

        #Hundreds
        hundreds = num//100
        num %= 100
        if hundreds >= 5:
            if hundreds == 9:
                ans += "CM"
            else:
                ans += "D"
                hundreds -= 5
                while hundreds > 0:
                    ans += "C"
                    hundreds -= 1
        elif hundreds == 4:
            ans += "CD"
        else:
            while hundreds > 0:
                ans += "C"
                hundreds -= 1

        #Tens    
        tens = num//10
        num %= 10
        if tens >= 5:
            if tens == 9:
                ans += "XC"
            else:
                ans += "L"
                tens -= 5
                while tens > 0:
                    ans += "X"
                    tens -= 1
        elif tens == 4:
            ans += "XL"
            
        else:
            while tens > 0:
                ans += "X"
                tens -= 1

        #Ones        
        if num >= 5:
            if num == 9:
                ans += "IX"
            else:
                ans += "V"
                num -= 5
                while num > 0:
                    ans += "I"
                    num -= 1
        elif num == 4:
            ans += "IV"
        else:
            while num > 0:
                ans += "I"
                num -= 1
        return ans
        