"""
Given a string str. 
Find the length of longest palindromic substring.
"""

def validPalindromeSubstring(str):
    max_length = 1
    for i in range(len(str)):
        max_length = max(expand(i, i, str), max_length)
        max_length = max(expand(i, i + 1, str), max_length)
    return max_length

# return longest length of substring with given center
def expand(i, j, str):
    length = 0
    while i>=0 and j<len(str) and str[i]==str[j]:
        length = j - i + 1
        i = i - 1
        j = j + 1
    return length

print(validPalindromeSubstring('validity'))
print(validPalindromeSubstring('gfecdabbadcefg'))
