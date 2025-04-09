# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countValid(self, start, end, word, vowels):
        window = Counter()
        count = 0
        for i in range(start, end):
            window[word[i]] += 1
            leftCount = 0

            while window >= vowels:
                leftCount += 1
                window[word[start]] -= 1
                start += 1
            count += leftCount * (end - i)

        return count

    
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        vowels = Counter(['a', 'e', 'i', 'o', 'u'])
        res = 0
        lastConsonant = -1

        for i in range(n):
            if word[i] not in vowels:
                res += self.countValid(lastConsonant + 1, i, word, vowels)
                lastConsonant = i
        
        res += self.countValid(lastConsonant + 1, n, word, vowels)
       
        return res