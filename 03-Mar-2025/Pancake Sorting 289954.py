# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        index = len(arr)
        ans = []

        while index > 0:
            max_index = arr.index(max(arr[: index]))
            if max_index != index-1:
                ans.append(max_index + 1)
                ans.append(index)
                arr = arr[max_index: : -1] + arr[max_index + 1: ]
                arr = arr[index-1: 0: -1]
    
                
                
            index -= 1
            
        return ans
