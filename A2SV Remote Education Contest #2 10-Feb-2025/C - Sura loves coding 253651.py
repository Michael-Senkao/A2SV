# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C



if __name__ == "__main__":
    
    n = int(input())
    encoded = input()
    
    actual = encoded[0] if n & 1 else ''
    index = 1 if actual else 0
    
    while index < n:
        actual = encoded[index] + actual
        index += 1
        if index < n:
            actual += encoded[index]
            index += 1
            
    print(actual)
           
    
    