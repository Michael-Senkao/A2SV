# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A


q = int(input())
for _ in range(q):
    l,r,d = map(int, input().split())
    
    ans = None
    if l > d:
        ans = d
    else:
        ans = d * ((r // d) + 1)
 
    print(ans)