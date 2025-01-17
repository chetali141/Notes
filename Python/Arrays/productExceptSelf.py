"""
Given an array, return the list of product of all the numbers in the array except the number itself.
"""

# Using the division
# def productExceptSelf(nums):
#     product = 1
#     zero = 0
#     res = [0]*len(nums)
#     for i in nums:
#         if i == 0:
#             zero += 1
#             if zero > 1:
#                 return [0] * len(nums)
#         else:
#             product = product * i
#     i = 0
#     for num in nums:
#         if zero > 0 and num != 0:
#             res[i] = 0
#         elif zero > 0 and num == 0:
#             res[i] = product
#         else:
#             res[i] = int(product/num)
#         i += 1
#     return res

def prefix(nums,res):
    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]
    return res

def suffix(nums,res):
    sf = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= sf
        sf *= nums[i]
    return res

#Using prefix and suffix approach
def productExceptSelf(nums):
    res = [1] * len(nums)
    res = suffix(nums,prefix(nums,res))
    return res

print(productExceptSelf([5,2,0,3,1]))
print(productExceptSelf([2,9,0,6,0,1]))
