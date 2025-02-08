# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq_chars = Counter(chars)
        sum_of_length = 0

        for word in words:
            curr_freq = Counter(word)
            if freq_chars >= curr_freq:
                sum_of_length += len(word)

        return sum_of_length