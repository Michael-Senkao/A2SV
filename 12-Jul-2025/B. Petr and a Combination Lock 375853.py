# Problem: B. Petr and a Combination Lock - https://codeforces.com/contest/1097/problem/B


from collections import deque

def dfs(pos, indx, degrees):
    if indx >= len(degrees):
        return pos == 0
    return dfs((pos + degrees[indx]) % 360, indx + 1, degrees) or dfs((pos - degrees[indx] + 360) % 360, indx + 1, degrees)


n = int(input())

degrees = []
for _ in range(n):
    degrees.append(int(input()))
print('YES' if dfs(0, 0, degrees) else 'NO')
