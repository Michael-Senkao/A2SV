# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b


n,k = map(int, input().split())
arr = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
  for j in range(i + 1, min(n, i + k + 1)):
    dp[j] = min(dp[j], dp[i] + abs(arr[i] - arr[j]))
  
print(dp[-1])