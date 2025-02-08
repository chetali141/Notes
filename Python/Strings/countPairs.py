"""
Given string 's', count the number of pairs such that: 
i < j, s[i] = 'a' and s[j] = 'g'

Concept used: carry forward
"""

def countPairs(s):
    n = len(s)
    countG = 0
    pairs = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'g':
            countG = countG + 1
        elif s[i] == 'a':
            pairs = pairs + countG
    return pairs

# print(countPairs('adgagagfg'))
