# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    evenCount = 0
    oddCount = 0
    
    for index, val in enumerate(arr):
        if val % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
            
        if oddCount and evenCount:
            arr.sort()
            break
        
    print(*arr)