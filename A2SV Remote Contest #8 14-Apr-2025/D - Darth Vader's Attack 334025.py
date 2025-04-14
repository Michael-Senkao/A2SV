# Problem: D - Darth Vader's Attack - https://codeforces.com/gym/599884/problem/D


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()

    leftL = []
    lCount = 0
    res = 0
    
    for i in range(n):
        if s[i] == 'L':
            lCount += 1
        leftL.append(lCount)
        
    rCount = 0
   
    for i in range(n-1, -1, -1):
        if s[i] == 'R':
            rCount += 1
        res += (min(rCount, leftL[i]) * a[i])
        
    print(res)