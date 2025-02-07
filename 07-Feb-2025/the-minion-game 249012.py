# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    # your code goes here
    n = len(string)
    stuart_score = 0
    kevin_score = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    for i in range(n):
        if string[i] in vowels:
            kevin_score += (n - i)  
        else:
            stuart_score += (n - i)  

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")
         

if __name__ == '__main__':
    s = input()
    minion_game(s)