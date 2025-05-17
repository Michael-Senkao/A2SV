# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A


import math

n,m,a = map(int, input().split())

l = math.ceil(n / a)
w = math.ceil(m / a)
print(l * w)