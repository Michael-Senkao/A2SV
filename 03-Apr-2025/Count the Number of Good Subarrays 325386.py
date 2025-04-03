# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        goodPairs = 0
        left = 0
        res = 0

        for right in range(n):
            # Add no. of good pairs that can be formed with current value
            goodPairs += freq[nums[right]]
            freq[nums[right]] += 1 # Update the frequency of current value

            rightCount = n - right
            while goodPairs >= k:
                res += n - right # Add all subrrays starting from left
                freq[nums[left]] -= 1 # Decrease the frequency of the left value
                goodPairs -= freq[nums[left]] # Remove the pairs formed by current left value
                left += 1 # Move to the next

        return res

                