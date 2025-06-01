# Problem: Domino Piling - https://codeforces.com/problemset/problem/50/A


m,n = map(int, input().split())


ans = (n // 2) * m
if n % 2 != 0:
    ans += m // 2

print(ans)