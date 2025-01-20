"""
Find an element in array using Binary Search.
"""

def binarySearch(nums, target):
    low = 0
    high = len(nums)
    mid = 0

    while low <= high:
        mid = (low + high)//2

        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return False

print(binarySearch([4,6,9,11,14,21,34,56,90,98],56))
print(binarySearch([4,6,9,11,14,21,34,56,90,98],23))
