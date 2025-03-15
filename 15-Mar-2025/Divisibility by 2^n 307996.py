# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D


def helper(index, product, k, moves, dp):
    
    if product % k == 0:
        return moves
    if index > n:
        return float('inf')
    if (index, product) in dp:
        return dp[(index,product)]
    take = helper(index + 1, product*index, k, moves + 1, dp)
    notTake = helper(index + 1, product, k, moves, dp)
    dp[(index,product)] = min(take, notTake)
    return dp[(index,product)]
    

if __name__ == '__main__':
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        dp = {}
        k = 2**n
        product = 1
        for num in arr:
            product *= num
        minMoves = helper(2, product, k, 0, dp)
        if minMoves <= n:
            print(minMoves)
        else:
            print(-1)