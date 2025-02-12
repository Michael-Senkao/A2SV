# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)

        symbol_to_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        index = 0
        while index < n - 1:
            first = symbol_to_value[s[index]]
            second = symbol_to_value[s[index + 1]]
            
            if first >= second:
                result += first
            else:
                result += second - first
                index += 1

            index += 1
        
        if index < n:
            result += symbol_to_value[s[index]]
        return result