# Problem: Cellular Network - https://codeforces.com/contest/702/problem/C


def solve(n,m,cities,towers):
    cities.sort()
    towers.sort()
    r = float('-inf')
    towerInd = 0
   
    for i in range(n):
        while towerInd < m and towers[towerInd] <= cities[i]:
            towerInd += 1
        
        nearest = cities[i] - towers[towerInd - 1] if towerInd > 0 else float('inf')
 
        if towerInd < m:
            nearest = min(nearest, towers[towerInd] - cities[i])
        r = max(r, nearest)
        towerInd = towerInd - 1 if towerInd > 0 else towerInd
        
    return r
    
if __name__ == '__main__':
    n,m = map(int, input().split())
    cities = list(map(int, input().split()))
    towers = list(map(int, input().split()))
    
    print(solve(n, m, cities, towers))