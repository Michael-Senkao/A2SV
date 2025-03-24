# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        t_freq = Counter(t)
        window_freq = Counter()

        left = 0
        minStart, minEnd = -1, len(s)

        for right in range(len(s)):
            window_freq[s[right]] += 1

            if window_freq >= t_freq:
                
                while window_freq >= t_freq:
                    window_freq[s[left]] -= 1
                    left += 1
               
                if right - left + 2 < minEnd - minStart + 1:
                    minStart, minEnd = left - 1, right

     
        return s[minStart: minEnd + 1] if minStart > -1 else ""