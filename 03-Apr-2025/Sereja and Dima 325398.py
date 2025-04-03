# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    
    left,right = 0, n - 1
    s,d = 0,0
    
    while left < right:
        l1 = l2 = a[left]
        r1 = r2 = a[right]
        
        if l1 > r1:
            s += l1
            left += 1
            l2 = a[left]
        else:
            s += r1
            right -= 1
            r2 = a[right]
        
        if l2 > r2:
            d += l2
            left += 1
        else:
            d += r2
            right -= 1
            
    if left == right:
        s += a[left]
        
    print(s,d)