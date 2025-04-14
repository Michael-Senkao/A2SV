# Problem: B - Lily and the check - https://codeforces.com/gym/592318/problem/B

import math
t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    p = math.ceil(math.log(y/x, 10))

   
    res = 0
    while y >= x:
        max_v = x*(10**p)
        while y >= max_v:
            res += 1
            y -= max_v
        p -= 1
    
    print(res + y)