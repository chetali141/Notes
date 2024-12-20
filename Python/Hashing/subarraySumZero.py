"""
Given an array
Check if there exists a subarray with sum = 0
"""

def subarraySumZero(nums):
    dist = {}
    dist[0] = 1
    sum = 0
    for idx in range(0,len(nums)):
        sum = sum + nums[idx]
        if sum in dist:
            return True
        else:
            dist[sum] = 1
    return False

# print(subarraySumZero([2,2,1,-3,4,3,1,-2,-3]))
# print(subarraySumZero([1,2,3,4]))
# print(subarraySumZero([1,2,-3,4,2,1]))
