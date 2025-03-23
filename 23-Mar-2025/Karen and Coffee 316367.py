# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B


    

if __name__ == '__main__':
    
    n,k,q = map(int, input().split())
    
    prefixSum = [0]*200003
    
    for _ in range(n):
        l,r = map(int, input().split())
        prefixSum[l] += 1
        prefixSum[r + 1] -= 1
        
    prefix = 0
    count = 0
    for i in range(200003):
        prefix += prefixSum[i]
        if prefix >= k :
            count += 1
        prefixSum[i] = count
        
    for _ in range(q):
        a,b = map(int, input().split())
        print(prefixSum[b] - prefixSum[a-1])
        
    