# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

from collections import defaultdict

n = int(input())
adjMat = []
adjList = defaultdict(list)

for _ in range(n):
    mat = [int(val) for val in input().split()]
    adjMat.append(mat)

for i in range(n):
    i
    for nei in range(n):
        if adjMat[i][nei]:
            adjList[i].append(nei + 1)

for i in range(n):
    print(len(adjList[i]), *adjList[i])