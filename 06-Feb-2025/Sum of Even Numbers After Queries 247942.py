# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even_sum,odd_sum = 0,0
        for num in nums:
            if num & 1:
                odd_sum += num
            else:
                even_sum += num

        res = []
        for val, index in queries:
            prev_val = nums[index]
            curr_val = prev_val + val

            if prev_val & 1:
                if curr_val & 1:
                    odd_sum += val
                else:
                    odd_sum -= prev_val
                    even_sum += curr_val
            elif curr_val & 1:
                even_sum -= prev_val
                odd_sum += curr_val
            else:
               even_sum += val

            nums[index] = curr_val
            res.append(even_sum) 

        return res
