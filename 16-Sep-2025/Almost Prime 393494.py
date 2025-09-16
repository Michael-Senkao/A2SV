# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

import math

n = int(input())

is_prime = [True] * (n + 1)
ans = 0

is_prime[0] = is_prime[1] = False

for i in range(2, n + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
            
for num in range(1, n + 1):
    prime_factors = set()
    for j in range(1, int(math.sqrt(num)) + 1):
        if num % j == 0:
            if is_prime[j]:
                prime_factors.add(j)
            if is_prime[num // j]:
                prime_factors.add(num // j)
        if len(prime_factors) > 2:
            break
                
    ans += len(prime_factors) == 2
    
print(ans)