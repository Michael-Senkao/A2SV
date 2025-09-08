# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 'YES'
    a.sort()
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            ans = 'NO'
            break
        
    print(ans)
            