""" 
Given an array and 'Q' queries with each query having 'L' and 'R' indexes and 'X'
where 'X' can be Odd or Even
Find sum for all 'X' index elements between L and R for all Q 
i.e. sum of all odd or even index elements between L and R

Concept used: prefix sum and carry forward.
"""

import helper

def sumRange(nums,l,r,x):
    n = len(nums)
    sum = 0
    pf = [0] * n

    if x == 'odd':
        for i in range(1, n):
            if i % 2 == 0:
                pf[i] == pf[i-1]
            else:
                pf[i] = pf[i-1] + nums[i]
        pf = helper.prefixSum(pf)
    elif x == 'even':
        pf[0] = nums[0] 
        for i in range(1, n):
            if i % 2 == 0:
                pf[i] = pf[i-1] + nums[i]
            else:
                pf[i] == pf[i-1]
        pf = helper.prefixSum(pf)
    else:
        return ('Wrong input')

    if l == 0:
        sum = pf[r]
    else:
        sum = pf[r] - pf[l]

    return sum

# print(sumRange([2,4,3,1,5],2,4,'odd'))
# print(sumRange([2,4,3,1,5],1,3,'even'))
# print(sumRange([2,4,3,1,5],3,4,'mno'))
