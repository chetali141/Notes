#  Given array - pick 'k' elements from left or right or both the sides of the array to get the maximum sum.

import helper

def maxSum(arr, k):
    mSum = arr[0]
    pf = helper.prefixSum(arr)
    sf = helper.suffixSum(arr)

    for x in range(0, k + 1):
        sum = 0
        before = 0 if x == 0 else pf[x - 1]
        after = 0 if x >= k else sf[len(arr) - (k - x)]
        
        sum = before + after

        if sum > mSum:
            mSum = sum

    return mSum

# print(maxSum([5,-2,3,1,2],2))
