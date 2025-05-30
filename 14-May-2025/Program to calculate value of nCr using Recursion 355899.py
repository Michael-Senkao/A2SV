# Problem: Program to calculate value of nCr using Recursion - https://www.geeksforgeeks.org/program-to-calculate-value-of-ncr-using-recursion/

def comb(n, r):
    if(n < r):
        return 0
    if(r == 0):
        return 1
    if(r == 1):
        return n
    if(n == 1):
        return 1
    return comb(n - 1, r - 1) + comb(n - 1, r)