"""
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.
"""

# TC of this approach is O(logn) - uses binary search
def peakElement(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

# TC of this approach is O(n)
def findPeakElement(nums):
    n = len(nums)
    max = nums[n-1]
    idx = n-1
    if n == 1:
        return 0
    for i in range(n-2, -1, -1):
        if max < nums[i]:
            max = nums[i]
            idx = i
    return idx
