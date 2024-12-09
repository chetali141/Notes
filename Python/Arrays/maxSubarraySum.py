# Return maximum sum from sum of all subarrays present within a given array

def subarraySum(nums):
    n = len(nums)
    max_sum = nums[0]
    for i in range(0, n):
        sum = 0
        for j in range(i, n):
            sum = sum + nums[j]
            if max_sum < sum:
                max_sum = sum
    return max_sum

# print(subarraySum([4,-11,1,6,2,3,-2]))
