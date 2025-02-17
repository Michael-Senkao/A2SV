# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C


password = input()

n = int(input())

start_letters = set()
end_letters = set()

for _ in range(n):
    x = input()
    start_letters.add(x[0])
    end_letters.add(x[1])
    if x == password or (password[0] in end_letters and password[1] in start_letters):
        print("YES")
        break
else:
    print("NO")