# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c


n = int(input())
vals = []
for _ in range(n):
  a,b,c = map(int, input().split())
  vals.append([a,b,c])
  

for i in range(1, n):
  vals[i][0] += max(vals[i-1][1], vals[i-1][2])
  vals[i][1] += max(vals[i-1][0], vals[i-1][2])
  vals[i][2] += max(vals[i-1][0], vals[i-1][1])

print(max(vals[-1]))
