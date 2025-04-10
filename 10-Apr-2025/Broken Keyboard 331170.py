# Problem: Broken Keyboard - https://codeforces.com/problemset/problem/1251/A


if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        s = input()
        
        workingChars = set()
        currCharCount = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                currCharCount += 1
            else:
                if currCharCount % 2 != 0:
                    workingChars.add(s[i - 1])
                    if len(workingChars) == 26:
                        break
                    
                currCharCount = 1
        
        if currCharCount % 2 != 0:
            workingChars.add(s[-1])
            
        print(''.join(sorted(workingChars)))