# Problem: A - Assem's Secret Code - https://codeforces.com/gym/586622/problem/A



if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
       s = input()
       
       print("YES" if s.lower() == 'yes' else "NO")
    