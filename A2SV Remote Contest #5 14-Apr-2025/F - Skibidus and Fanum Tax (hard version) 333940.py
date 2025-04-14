# Problem: F - Skibidus and Fanum Tax (hard version) - https://codeforces.com/gym/592318/problem/F


def solve(min_v, num):
    left,right = 0, m - 1
    bestJ = m

    while left <= right:
        mid = left + (right - left) // 2
        if b[mid] - num < min_v:
            left = mid + 1
        else:
            bestJ = mid
            right = mid - 1
    
    return bestJ

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()

    a[0] = min(a[0], b[0] - a[0])

    for i in range(1, n):
        bestJ = solve(a[i-1], a[i])
        val,best = a[i], a[i]
        if bestJ < m:
            best = b[bestJ] - val
            
        if val >= a[i-1]:
            if best >= a[i-1]:
                a[i] = min(val, best)
        elif best >= a[i-1]:
            a[i] = best
        else:
            print('NO')
            break
    else:
        print('YES')
        