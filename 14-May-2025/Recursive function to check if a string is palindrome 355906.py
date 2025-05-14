# Problem: Recursive function to check if a string is palindrome - https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/

# Recursive util function to check if a string is a palindrome
def isPalindromeUtil(s, left, right):

    # Base case
    if left >= right:
        return True
    
    # If the characters at the current positions 
    # are not equal, it is not a palindrome
    if s[left] != s[right]:
        return False

    # Move left pointer to the right
    # and right pointer to the left
    return isPalindromeUtil(s, left + 1, right - 1)