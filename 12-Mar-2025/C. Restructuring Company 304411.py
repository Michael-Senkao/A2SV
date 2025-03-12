# Problem: C. Restructuring Company - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C


class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1]*(n+1)
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
        
    def union(self, x,y):
        parX = self.find(x)
        parY = self.find(y)
        
        if parX != parY:
            if self.rank[parX] > self.rank[parY]:
                self.parent[parY] = parX
            elif self.rank[parY] > self.rank[parX]:
                self.parent[parX] = parY
            else:
                self.parent[parY] = parX
                self.rank[parX] += 1
            return True
            
        return False

    
if __name__ == '__main__':
    
    n,q = map(int, input().split())
    dsu = DSU(n)
    
    for _ in range(q):
        type,x,y = map(int, input().split())
        if type == 1:
            dsu.union(x,y)
        elif type == 2:
            for y in range(x+1, y+1):
                dsu.union(x,y)
        elif dsu.find(x) == dsu.find(y):
            print("YES")
        else:
            print("NO")
        
    