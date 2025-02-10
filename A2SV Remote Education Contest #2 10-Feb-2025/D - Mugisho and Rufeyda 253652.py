# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D



if __name__ == "__main__":
    
    n,t = map(int, input().split())
    num = int('9' * n)
    rem = num % t
   
    num = str(num - (num % t))
    print(num if (int(num) > 0 and len(num) == n) else -1)
    
    
    