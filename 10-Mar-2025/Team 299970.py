# Problem: Team - https://codeforces.com/contest/231/problem/A



    
if __name__ == '__main__':
    n = int(input())
    
    maxSolved = 0
    for _ in range(n):
        knows = sum(map(int, input().split()))
        maxSolved += knows > 1
        
    print(maxSolved)