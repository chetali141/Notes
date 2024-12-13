"""
Given a string s, return true if it is a palindrome, otherwise return false.
Consider it to be case-insensitive and ignore all non-alphanumeric characters.
"""

def validPalindrome(s):
    s = ''.join(ch for ch in s if ch.isalnum())
    i = 0
    j = len(s) - 1

    while i<j:
        if s[i].lower() != s[j].lower():
            return False
        j = j - 1
        i = i + 1
        
    return True

print(validPalindrome('cat tac!! bye'))
print(validPalindrome('was saw?'))
