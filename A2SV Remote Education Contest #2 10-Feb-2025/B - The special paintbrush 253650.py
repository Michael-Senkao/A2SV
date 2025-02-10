# Problem: B - The special paintbrush - https://codeforces.com/gym/586622/problem/B



if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        s = input()
        
        start_index = s.find('B')
        
        if start_index == -1:
            print(0)
        else:
            
            end_index = start_index
            for i in range(start_index, n):
                if s[i] == 'B':
                    end_index = i
            print(end_index - start_index + 1)
           
    
    