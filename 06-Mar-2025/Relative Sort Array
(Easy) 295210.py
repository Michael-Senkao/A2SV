# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def customComparator(item):
            return arr2_indices.get(item, item + n2)

        arr2_indices = {num: ind for ind, num in enumerate(arr2)}
        n2 = len(arr2)
        arr1.sort(key = customComparator)
        return arr1