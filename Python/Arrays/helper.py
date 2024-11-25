
def prefixSum(nums):
    pf = [0] * len(nums)
    pf[0] = nums[0]
    for idx in range(1,len(nums)):
        pf[idx] = pf[idx-1] + nums[idx]
    return pf
