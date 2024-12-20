"""
Also c/a Two Sum problem 

given an array and a number k, return true if there exist a pair such that 
i != j
nums[i] + nums[j] = k
"""

def pairSumTarget(nums, k):
    dictDiff = {}
    for i in nums:
        temp = k - i
        if temp in dictDiff:
            return True
        else:
            dictDiff[i] = 1
            print(dictDiff)
    return False


# print(pairSumTarget([2,7,11,15],18))
# print(pairSumTarget([1,2,8,6,7,3],12))
# print(pairSumTarget([2,3,6,7,2,1],4))
