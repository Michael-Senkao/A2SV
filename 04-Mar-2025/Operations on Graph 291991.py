# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

from collections import defaultdict
n = int(input())
k = int(input())

graph = defaultdict(list)
for _ in range(k):
    query = [int(x) for x in input().split()]
    
    if query[0] == 1:
        u,v = query[1:]
        graph[u].append(v)
        graph[v].append(u)
    else:
        u = query[1]
        print(*graph[u])
