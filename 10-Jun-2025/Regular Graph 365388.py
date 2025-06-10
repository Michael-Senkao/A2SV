# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076


n,m = map(int, input().split())

degree = [0] * n
for _ in range(m):
    u,v = map(int, input().split())
    degree[u - 1] += 1
    degree[v - 1] += 1

ans = 'YES'
for deg in degree:
    if deg != degree[0]:
        ans = 'NO'
        break
print(ans)
