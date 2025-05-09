# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

#User function Template for python3

class Solution:
    def removeUtil (self, S):
        #code here
        if len(S) < 2:
            return S
        
        n = len(S)
        temp = []
        duplicates = False
        i = 0
        while i < n - 1:
            if S[i] != S[i+1]:
                temp.append(S[i])
            else:
                duplicates = True
                while i < n - 1 and S[i] == S[i+1]:
                    i += 1
            i += 1
        if i < n: 
            temp.append(S[i])
        return self.removeUtil(''.join(temp)) if duplicates else ''.join(temp)
