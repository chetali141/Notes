# Rotate given array 'k' times from Left to Right - inplace

import reverseArray

def rotateKTime(arr, k):
    n = len(arr)
    k = k % n

    arr = reverseArray.reversePortion(arr, 0, n-k-1)
    arr = reverseArray.reversePortion(arr, n-k, n-1)
    arr = reverseArray.reversePortion(arr, 0, n-1)
    return arr

# print(rotateKTime([1,2,3,4,5,6],4))
