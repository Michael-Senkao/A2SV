# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a


n = int(input())
arr = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
  if i + 1 < n:
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(arr[i] - arr[i + 1]))
  if i + 2 < n:
    dp[i + 2] = min(dp[i + 2], dp[i] + abs(arr[i] - arr[i + 2]))
  
print(dp[-1])