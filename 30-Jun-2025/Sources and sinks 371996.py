# Problem: Sources and sinks - https://basecamp.eolymp.com/en/problems/3986


n = int(input())
adjMatrix = []
sources = []
sinks = []
for _ in range(n):
    row = list(map(int, input().split()))
    adjMatrix.append(row)

for v in range(n):
    for r in range(n):
        if adjMatrix[r][v]:
            break
    else:
        sources.append(v + 1)

    for c in range(n):
        if adjMatrix[v][c]:
            break
    else:
        sinks.append(v + 1)
        
print(len(sources), *sources)
print(len(sinks), *sinks)