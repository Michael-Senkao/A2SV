# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = [(-frequency, word) for word,frequency in Counter(words).items()]
        heapify(heap)
        ans = []

        while k:
            _,word = heappop(heap)
            ans.append(word)
            k -= 1
        return ans