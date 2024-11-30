
def prefixSum(nums):
    pf = [0] * len(nums)
    pf[0] = nums[0]
    for idx in range(1,len(nums)):
        pf[idx] = pf[idx-1] + nums[idx]
    return pf

def suffixSum(nums):
    sf = [0] * len(nums)
    sf[len(nums)-1] = nums[-1]
    for idx in range(len(nums)-2,-1,-1):
        sf[idx] = sf[idx + 1] + nums[idx]
    return sf
