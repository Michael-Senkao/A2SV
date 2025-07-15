# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        first_max_ind = first_min_ind = second_max_ind = second_min_ind = None

        if arrays[0][0] < arrays[1][0]:
            first_min_ind = 0
            second_min_ind = 1
        else:
            first_min_ind = 1
            second_min_ind = 0

        if arrays[0][-1] > arrays[1][-1]:
            first_max_ind = 0
            second_max_ind = 1
        else:
            first_max_ind = 1
            second_max_ind = 0

        for i in range(2, n):
            if arrays[i][0] < arrays[first_min_ind][0]:
                second_min_ind = first_min_ind
                first_min_ind = i
            elif arrays[i][0] < arrays[second_min_ind][0]:
                second_min_ind = i

            if arrays[i][-1] > arrays[first_max_ind][-1]:
                second_max_ind = first_max_ind
                first_max_ind = i
            elif arrays[i][-1] > arrays[second_max_ind][-1]:
                second_max_ind = i

        if first_max_ind != first_min_ind:
            return arrays[first_max_ind][-1] - arrays[first_min_ind][0]
        
        return max(arrays[first_max_ind][-1] - arrays[second_min_ind][0], arrays[second_max_ind][-1] - arrays[first_min_ind][0])
