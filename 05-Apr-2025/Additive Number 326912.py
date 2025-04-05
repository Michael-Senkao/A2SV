# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(index, currNum, sequence):
    
            if index == len(num):
                sequence.append(currNum)
                c = check(sequence)
                sequence.pop()
                
                return c
            if len(sequence) > 2 and not check(sequence):
                return False
            extend = backtrack(index + 1, currNum + num[index], sequence)
            if extend: return True

            sequence.append(currNum)
            not_extend = backtrack(index + 1, num[index], sequence)
            sequence.pop()

            return not_extend

        def check(sequence):
            if len(sequence) < 3:
                return False
            frist = second = None
            if sequence[0].startswith('0') and len(sequence[0]) > 1:
                return False
        
            first = int(sequence[0])

            if sequence[1].startswith('0') and len(sequence[1]) > 1:
                return False
        
            second = int(sequence[1])
            for val in sequence[2:]:
                if val.startswith('0') and len(val) > 1:
                    return False
                val = int(val)
                if val != first + second:
                    return False
                first, second = second, val

            return True

        return backtrack(1, num[0], [])

            
            