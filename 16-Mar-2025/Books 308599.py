# Problem: Books - https://codeforces.com/contest/279/problem/B


    

if __name__ == '__main__':
    
    n,t = map(int, input().split())
    a = list(map(int, input().split()))
    
    left = 0
    windowSum = 0
    res = 0
    for right in range(n):
        windowSum += a[right]
        while windowSum > t:
            windowSum -= a[left]
            left += 1
        res = max(res, right - left + 1)
        
    print(res)