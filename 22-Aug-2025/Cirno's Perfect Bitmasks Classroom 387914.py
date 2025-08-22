# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

import math

t = int(input())

for _ in range(t):
    x = int(input())
    
    if x == 1:
        print(3)
    else:
        k = int(math.log(x, 2))
        pow_val = pow(2,k)
        bits = bin(x)[2:]
        first_one_position = len(bits) - bits.rfind('1') - 1
        
        min_val = pow(2, first_one_position)
        if x == pow_val:
            print(min_val + 1)
        else:
            print(min_val)
            