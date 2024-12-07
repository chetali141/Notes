#Print all subarrays of length 'k' present in a given array
 
def subarrayK(nums, k):
    n = len(nums)
    for i in range(0, n - k + 1):
        print(nums[i:(k+i)])

subarrayK([5,16,21,33,69,81,23,31,54], 4)

