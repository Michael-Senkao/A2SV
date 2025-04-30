# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

import sys
from collections import defaultdict

#----------------- INPUT -----------------
data = sys.stdin.read().splitlines()
n,k = map(int, data[0].split())
a = list(map(int, data[-1].split()))

#----------------- SOLUTION -------------------
left = 0
start = end = 0
freq = defaultdict(int)
for right in range(n):
    freq[a[right]] += 1
    while len(freq) > k:
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            del freq[a[left]]
            
        left += 1
    if right - left > end - start:
        start, end = left, right
        
print(start + 1, end + 1)