# Problem: Honest Coach - https://codeforces.com/problemset/problem/1360/B


    

if __name__ == '__main__':
    
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        
        s.sort()
        res = float('inf')
        
        for i in range(1, n):
            res = min(res, s[i] - s[i-1])
        
        print(res)
    
