# Given an array find the sum of all subarray sum

def allSubarraySum(nums):
    sum = 0
    for i in range(0, len(nums)):
        noSubarray = (i + 1) * (len(nums) - i)        
        sum = sum + (nums[i] * noSubarray)
    return sum

print(allSubarraySum([3,2,1,6,-1,4]))
