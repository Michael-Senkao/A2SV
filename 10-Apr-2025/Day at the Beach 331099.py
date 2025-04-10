# Problem: Day at the Beach - https://codeforces.com/problemset/problem/599/C


if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    
    maxLeft = []
    currMax = -1  
    splits = 0
    
    for i in range(n):
        maxLeft.append(currMax)
        currMax = max(currMax, heights[i])
        
    currMin = float('inf')
    
    for i in range(n-1, -1, -1):
        currMin = min(currMin, heights[i])
        if currMin >= maxLeft[i]:
            splits += 1
            
    print(splits)