# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C



if __name__ == "__main__":
    
    n,k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    arr.sort()
    if k == 0:
        print(1 if arr[0] > 1 else -1)
    elif k < n and arr[k-1] == arr[k]:
        print(-1)
    else:
        print(arr[k - 1])