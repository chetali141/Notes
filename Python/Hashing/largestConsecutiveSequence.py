"""
Given an array,
find the largest sequence which can be rearranged to form a sequence of consecutive numbers
"""

def largestConsecutiveSequence(nums):
    count = 0
    
    s = set(nums)
    print(s)

    for i in range(0, len(nums)):
        if nums[i]-1 not in s:
            j = nums[i]
            while j in s:
                j = j + 1
            count = max(count, j-nums[i]) 

    return count

print(largestConsecutiveSequence([100,4,200,1,3,2,101,4,100]))
print(largestConsecutiveSequence([5,10,11,31,56,99,98,42,100]))
