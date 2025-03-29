# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        myDict ={0: -1}
        _sum = 0

        for i in range(n):
            _sum += nums[i]
            remainder = _sum % k
            if remainder in myDict:
                if i - myDict[remainder] > 1:
                    return True
            else:
                myDict[remainder] = i

        return False