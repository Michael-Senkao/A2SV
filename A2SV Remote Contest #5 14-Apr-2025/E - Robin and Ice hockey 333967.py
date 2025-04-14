# Problem: E - Robin and Ice hockey - https://codeforces.com/gym/592318/problem/E

from collections import defaultdict

home = input()
away = input()

n = int(input())

cards_home = defaultdict(int)
cards_away = defaultdict(int)


for _ in range(n):
    t,team,player_no,card = input().split()
    t = int(t)
    player_no = int(player_no)
    
    
    if team == 'h':
        if cards_home[player_no] == -1:
            continue
        if card == 'y':
            cards_home[player_no] += 1
        else:
            cards_home[player_no] += 2
        if cards_home[player_no] >= 2:
            cards_home[player_no] = -1
            print(home, player_no, t)
            
    else:
        if cards_away[player_no] == -1:
            continue
        if card == 'y':
            cards_away[player_no] += 1
        else:
            cards_away[player_no] += 2
        if cards_away[player_no] >= 2:
            cards_away[player_no] = -1
            print(away, player_no, t)
            