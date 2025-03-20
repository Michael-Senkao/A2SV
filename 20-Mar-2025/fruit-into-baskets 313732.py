# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        nums_dict = {}
        left = 0
        res = 0

        for right in range(n):
            fruit = fruits[right]
            nums_dict[fruit] = nums_dict.get(fruit, 0) + 1

            while len(nums_dict) > 2:
                nums_dict[fruits[left]] -= 1
                if nums_dict[fruits[left]] == 0:
                    del nums_dict[fruits[left]]

                left += 1

            res = max(res, right - left + 1)

        return res

        