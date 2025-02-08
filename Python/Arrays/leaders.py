"""
An element is called as leader if it is strictly greater than all the elements to its right.
Given an array of length 'n', find the leader and total number of leaders in array.

Concept used: suffix max.
"""

def leaders(nums):
    n = len(nums)
    max = nums[n-1]
    count = 1
    for i in range(n-2, -1, -1):
        if nums[i] > max:
            max = nums[i]
            count = count + 1
    return max, count

print(leaders([16,18,18,6,5,7,3]))
