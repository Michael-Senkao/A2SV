# Problem: Team - https://codeforces.com/contest/231/problem/A


if __name__ == "__main__":
    n = int(input())
    
    total_implemented = 0
    for _ in range(n):
        sure_friends = list(map(int, input().split()))
        
        if sum(sure_friends) > 1:
            total_implemented += 1
            
    print(total_implemented)
    