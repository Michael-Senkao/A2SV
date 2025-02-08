# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from typing import List

def countPairs(n: int, arr: List[int]) -> int:
    diff_count = {}
    pair_count = 0
    
    for index,value in enumerate(arr):
        diff = value - index
        diff_count[diff] = diff_count.get(diff, 0) + 1
        
    for count in diff_count.values():
        pair_count += count * (count - 1) // 2
    
    return pair_count

if __name__ == "__main__":
    t = int(input())
    
    strength_to_bonus = []
    for _ in range(t):
       n = int(input())
       
       arr = list(map(int, input().split()))
       
       print(countPairs(n, arr))
    