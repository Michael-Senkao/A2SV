# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B



    
if __name__ == '__main__':
    
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    c = [0]*m
    i,j = 0,0
    
    for j in range(m):
        while i < n and a[i] < b[j]:
            i+= 1
        c[j] = i
    print(*c)
            