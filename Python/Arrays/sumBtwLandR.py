""" 
Given an array and 'Q' queries with each query having 'L' and 'R' indexes.
Find sum for all elements between L and R for all Q

Concept used: prefix sum
"""

import helper

def sumBtwLandR(arr, l, r):
    pfSum = helper.prefixSum(arr)
    if l == 0:
        sum = pfSum[r]
    else:
        sum = pfSum[r] - pfSum[l-1]
    return sum

# print(sumBtwLandR([1,2,3,4,5,6,7], 0, 1))
# print(sumBtwLandR([1,2,3,4,5,6,7,8], 2, 5))
# print(sumBtwLandR([1,2,3,4,5,6,7], 5, 6))
# print(sumBtwLandR([1,2,3,4,5,6,7], 0, 6))
