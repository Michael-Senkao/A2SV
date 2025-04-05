# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B


if __name__ == '__main__':
    n,d = map(int, input().split())
    
    friends = []
    for _ in range(n):
        m,s = map(int, input().split())
        friends.append((m,s))
    
    left = 0
    maxFactor = 0
    currFactor = 0
    friends.sort()
    
    for right in range(n):
        currFactor += friends[right][1]
        while friends[right][0] - friends[left][0] >= d:
            currFactor -= friends[left][1]
            left += 1
            
        maxFactor = max(maxFactor, currFactor)
        
    print(maxFactor)