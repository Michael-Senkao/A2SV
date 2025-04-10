# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        lastOddIndex = -1
        oddCount = 0
        left = 0
        niceCount = 0

        for right in range(n):
            if nums[right] % 2 == 0:
                continue

            oddCount += 1
            while oddCount > k:
                niceCount += right - lastOddIndex
                if nums[left] & 1:
                    oddCount -= 1
                left += 1

            lastOddIndex = right

        while oddCount == k:
            niceCount += n - lastOddIndex
            if nums[left] & 1:
                oddCount -= 1
            left += 1
        return niceCount

        