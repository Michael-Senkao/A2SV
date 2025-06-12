# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
adjMat = [[0 for _ in range(n)] for _ in range(n)]
for v in range(n):
    degree, *neigs = map(int, input().split())
    for nei in neigs:
        adjMat[v][nei-1] = 1

for v in adjMat:
    print(*v)
