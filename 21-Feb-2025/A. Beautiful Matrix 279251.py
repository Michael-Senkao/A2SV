# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A


def solve(row, r, target_row,target_col):
    for c in range(5):
        if row[c] == '1':
            min_moves = abs(target_row - r) + abs(target_col - c)
            print(min_moves)
            return True
            
    return False
    
if __name__ == "__main__":
    
    for r in range(5):
        row = input().split()
        
        if solve(row, r, 2, 2):
            break