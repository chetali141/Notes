"""
Return maximum sum from sum of all subarrays of length 'k' present within a given array

Concept used: sliding window.
"""

def subarraySum(nums, k):
    sum = 0
    for i in range(0, k):
        sum = sum + nums[i]
    max_sum = sum
    for i in range(k, len(nums)):
        sum = sum + nums[i] - nums[i-k]
        if max_sum < sum:
            max_sum = sum
    return max_sum

# print(subarraySum([ 1, 4, 2, 10, 2, 3, 1, 0, 20], 4))
