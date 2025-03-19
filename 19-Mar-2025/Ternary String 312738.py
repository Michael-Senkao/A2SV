# Problem: Ternary String - https://codeforces.com/gym/455166/problem/D


    

if __name__ == '__main__':
    
    n,s = map(int, input().split())
    a = list(map(int, input().split()))
    
    windowSum = 0
    left = 0
    maxLen = 0
    
    for right in range(n):
        windowSum += a[right]
        while windowSum > s:
            windowSum -= a[left]
            left += 1
            
        maxLen = max(maxLen, right - left + 1)
        
    print(maxLen)