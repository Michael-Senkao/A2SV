# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A



if __name__ == "__main__":
    
    n,m = map(int, input().split())
    
    end = True
    output = []
    for r in range(n):
        if r % 2 == 0:
            output = ['#'] * m
        else:
            output = ['.' ] * m
            
            if end:
                output[-1] = '#'
                end = False
            else:
                output[0] = '#'
                end = True
                
        print("".join(output))