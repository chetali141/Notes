# Return maximum sum from sum of all subarrays of length 'k' present within a given array

def subarraySum(nums, k):
    n = len(nums)
    max_sum = nums[0]
    for i in range(0, n - k + 1):
        sum = 0
        for j in range(i, k + i):
            sum = sum + nums[j]
            if max_sum < sum:
                max_sum = sum
    return max_sum

print(subarraySum([ 1, 4, 2, 10, 2, 3, 1, 0, 20], 4))
