# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E


    

if __name__ == '__main__':
    
    t = int(input())
    
    for _ in range(t):
        n,k = map(int, input().split())
        a = list(map(int, input().split()))
        x = list(map(int, input().split()))
        
        x_to_a = [(abs(x[i]), a[i]) for i in range(n)]
        
        x_to_a.sort()
        shots = 0
      
        
        for time, energy in x_to_a:
            bullets = k*time
            if bullets - shots < energy:
                print("NO")
                break
            shots += energy
        else:
            print("YES")
        
    