# Problem: B - The best for Geleta - https://codeforces.com/gym/590201/problem/B

import heapq

t =int(input())

for _ in range(t):
    n,m = map(int, input().split())
    arr = set(map(int, input().split()))
    
    maxV = max(arr)
    
    for _ in range(m):
        sign,l,r = input().split()
        l = int(l)
        r = int(r)
        
        if l <= maxV <= r:
            if sign == '-':
                maxV -= 1
            else:
                maxV += 1

        print(maxV, end=" ")


    print()
    

