"""
Given an array, find the smallest continuous part of the array such that it contains the minimum and maximum values of the array.
"""

def closestMinMax(nums):
    n = len(nums)
    length = n
    cMax = -1
    minimum = min(nums)
    maximum = max(nums)

    for i in range(n-1, -1, -1):
        if nums[i] == maximum:
            cMax = i
        if nums[i] == minimum:
            length = min(length, cMax - i + 1)

    return length

print(closestMinMax([1,2,3,1,3,4,6,4,6,3]))
print(closestMinMax([1,3,8,9,12,5,6,4,30]))
print(closestMinMax([36,99,63,54,77,89,49]))
