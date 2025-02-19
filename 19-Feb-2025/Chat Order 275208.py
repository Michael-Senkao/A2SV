# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B



if __name__ == "__main__":
    n = int(input())
    
    friend_list = []
    for _ in range(n):
        friend = input()
        friend_list.append(friend)
    
    talked_to = set()
    
    while friend_list:
        if friend_list[-1] not in talked_to:
            friend = friend_list[-1]
            print(friend)
            talked_to.add(friend)
        friend_list.pop()