# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

from collections import defaultdict,deque
n = int(input())
a = list(map(int, input().split()))

found = defaultdict(deque)
player_sum = sum(a)*2 // n

i = 0
while i < n:
    need = player_sum - a[i]
    if need in found:
        print(found[need][0], i + 1)
        found[need].popleft()
        if not found[need]:
            del found[need]
    else:
        found[a[i]].append(i + 1)

    i += 1
