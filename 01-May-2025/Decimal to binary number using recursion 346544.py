# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

def dec_to_bin(num):
    if num == 0:
        return 0
    else:
        return (num % 2 + 10 * dec_to_bin(num // 2))