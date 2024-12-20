"""
Given an array
Return the first non repeating element in the array
"""

def nonRepeatingElement(nums):
    dist = {}
    for i in nums:
        if i in dist:
            dist[i] = dist[i] + 1
        else:
            dist[i] = 1
    
    for i in dist:
        if dist[i] == 1:
            return i

    return None

# print(nonRepeatingElement([8,2,8,3,1,2,6,5]))
