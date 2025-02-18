# Problem: String Comperession - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        count = 1
        index = 0

        for i in range(1, n):
            if chars[i] != chars[i - 1]:
                
                chars[index] = chars[i - 1]
                index += 1
                if count > 1:
                    count = str(count)
                    for num in count:
                        chars[index] = num
                        index += 1

                count = 1
                
            else:
                count += 1

        chars[index] = chars[-1]
        index += 1
        if count > 1:
            count = str(count)
            for num in count:
                chars[index] = num
                index += 1
        
        return index