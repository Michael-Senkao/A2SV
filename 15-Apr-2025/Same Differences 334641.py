# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D


from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    res = 0
    diff = defaultdict(int)
    for index, num in enumerate(a):
        diff[num - index] += 1
        
    for count in diff.values():
        res += (count * (count - 1) // 2)
        
    print(res)