# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def getHash(self, string):
        char_freq = [0]*26
        
        for char in string:
            char_freq[ord(char) - 97] += 1
        return tuple(char_freq)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            hash_ = self.getHash(string)
            anagrams[hash_].append(string)
       
        return list(anagrams.values())