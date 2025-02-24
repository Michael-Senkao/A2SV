# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())

total_roads = 0
adjacency_matrix = []
for i in range(n):
    roads = list(map(int, input().split()))
    adjacency_matrix.append(roads)

for r in range(n):
    for c in range(r+1, n):
        total_roads += adjacency_matrix[r][c]
        
print (total_roads)

