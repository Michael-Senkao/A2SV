# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        def binary_search(left, right):
            if left < right:
                mid = left + (right - left)//2
                if letters[mid] > target:
                    right = mid
                else:
                    left = mid + 1
                return binary_search(left, right)
            return letters[left] if letters[left] > target else letters[0]

        return binary_search(0, len(letters) - 1)
        