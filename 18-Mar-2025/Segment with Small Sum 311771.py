# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A


    

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