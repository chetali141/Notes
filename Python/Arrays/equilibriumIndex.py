""" 
'i' is equilibrium index if sum of all elements on it's left is equal to the sum of all the elements on it's right

Concept used: prefix sum
"""

import helper

def equilibriumIndex(arr):
    idxCount = 0
    idxList = []
    n = len(arr)
    pfSum = helper.prefixSum(arr)

    for i in range(0,n):
        beforeSum = 0 if i == 0 else pfSum[i-1]
        afterSum = 0 if i > (n - 1) else (pfSum[n-1] - pfSum[i])
        if beforeSum == afterSum:
            idxCount = idxCount + 1
            idxList.append(i)

    return idxCount,idxList

# print(equilibriumIndex([1,2,3,4,2,3,1,9,6]))
