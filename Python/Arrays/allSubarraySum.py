"""
Given an array find the sum of all subarray sum

No of subarray with idx 'i' = (i+1)*(n-i)

Concept used: contribution of each element of array to answer
"""

def allSubarraySum(nums):
    sum = 0
    for i in range(0, len(nums)):
        noSubarray = (i + 1) * (len(nums) - i)        
        sum = sum + (nums[i] * noSubarray)
    return sum

print(allSubarraySum([3,2,1,6,-1,4]))
