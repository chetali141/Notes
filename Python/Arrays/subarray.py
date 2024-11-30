# Generate all subarrays in a given array

def subarray(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(i, n):
            print(nums[i:j+1])

# subarray([1,2,3,4,5,6])
