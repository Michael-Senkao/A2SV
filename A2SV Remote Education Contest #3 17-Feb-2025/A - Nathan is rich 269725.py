# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A


t = int(input())
for _ in range(t):
    n = int(input())

    minimum_vehecle = n // 4 
    n %= 4
    minimum_vehecle += n // 2
    print(minimum_vehecle)