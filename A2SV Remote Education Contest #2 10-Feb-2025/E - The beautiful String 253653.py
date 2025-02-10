# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E


def removeOne(index,s,pattern_start):
    if index - 1 >= 0 and index + 2 < len(s):
        if s[index - 1] and not s[index + 1] and not s[index + 2]:
            pattern_start.remove(index - 1)
    if index + 3 < len(s):
        if s[index + 1] and not s[index + 2] and not s[index + 3]:
            pattern_start.remove(index)

def removeZero(index, s, pattern_start):
    
    if index + 1 < len(s) and index - 2 >= 0:
        if s[index - 1] and s[index - 2] and not s[index + 1]:
            pattern_start.remove(index - 2)
    if index - 3 >= 0:
        if s[index - 2] and s[index - 3] and not s[index - 1]:
            pattern_start.remove(index - 3)
    
def matched(i):
    return s[i] and s[i + 1] and not s[i + 2] and not s[i + 3]

if __name__ == "__main__":
    
    t = int(input())
    
    for _ in range(t):
        s = list(map(int, list(input())))
       
        q = int(input())
        
        pattern_start = set()
        
        for i in range(len(s) - 3):
            if matched(i):
                pattern_start.add(i)
        
        for _ in range(q):
            ind,val = map(int, input().split())
            ind -= 1
            
            
            if s[ind]:
                removeOne(ind, s, pattern_start)
            else:
                removeZero(ind, s, pattern_start) 
            
            s[ind] = val
            for i in range(max(0, ind - 3), min(len(s) - 3, ind + 1)):
                if matched(i):
                    pattern_start.add(i)
           
            if len(pattern_start) > 0:
                print("YES")
            else:
                print("NO")
            
                    
                
    
    
    