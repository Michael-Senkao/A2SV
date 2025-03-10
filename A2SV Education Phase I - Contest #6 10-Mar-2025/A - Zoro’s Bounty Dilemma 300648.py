# Problem: A - Zoro’s Bounty Dilemma - https://codeforces.com/gym/594356/problem/A



    
if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        s = input()
        
        i = 0
        while i < len(s) and s[i] == '=':
            i += 1
        if i == len(s):
            print('=')
            continue
        j = i
        while j < len(s) and (s[j] == s[i] or s[j] == '='):
            j += 1
        if j < len(s):
            print('?')
        else:
            print(s[i])