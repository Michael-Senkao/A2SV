# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A



if __name__ == "__main__":
    target_row,target_col = 2,2
    
    for r in range(5):
        row = input().split()
        
        for c in range(5):
            if row[c] == '1':
                
                min_moves = abs(target_row - r) + abs(target_col - c)
                print(min_moves)