# Problem: Previous Permutation With One Swap - https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 1:
            return arr

        minInd = n - 1
        swap1, swap2 = -1, -1

        for i in range(n-2, -1, -1):
            if arr[i] > arr[minInd]:
                swap1 = i
                break
            minInd = i

       
        if swap1 == -1:
            return arr
        
        swap2 = minInd
        for j in range(swap1 + 1, n):
            if arr[j] < arr[swap1] and arr[j] > arr[swap2]:
                swap2 = j

      
        arr[swap1],arr[swap2] = arr[swap2], arr[swap1]
        return arr
        