# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

from typing import List

def canMoveNext(n: int, s:int, strength_to_bonus: List[tuple]) -> bool:
    
    strength_to_bonus.sort()
    for strength, bonus in strength_to_bonus:
        if s <= strength:
            return False
        s += bonus
    return True

if __name__ == "__main__":
    s,n = map(int, input().split())
    
    strength_to_bonus = []
    for _ in range(n):
        x,y = map(int,input().split())
        
        strength_to_bonus.append((x,y))
        
    if canMoveNext(n, s, strength_to_bonus):
        print("YES")
    else:
        print("NO")
    