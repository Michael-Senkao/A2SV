# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D


t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        res = [[0 for _ in range(n)] for _ in range(n)]
        curr = 1

        for c in range(n):
            vals = [curr + i for i in range(n)]
            curr += n
            left,right = 0, len(vals) - 1
            for r in range(n - 1):
                if r & 1:
                    res[r][c] = vals[right]
                    right -= 1
                else:
                    res[r][c] = vals[left]
                    left += 1
            
            if c & 1:
                res[n - 1][c-1] = vals[left]
            else:
                if c + 1 < n:
                    res[n - 1][c + 1] = vals[left]
                else:
                    res[n-1][c] = vals[left]

        if n & 1:
            res[n-1][0],res[n-1][n-1] = res[n - 1][n-1],res[n - 1][0]
        
        for row in res:
            print(*row)
