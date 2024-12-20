# Given an array, count distinct elements in the array.

"""
Solution approach
1. using dictionary (done below)
2. using sets i.e. return len(set(nums))
"""

def distinctElements(nums):
    dist = {}
    for i in nums:
        if i in dist:
            dist[i] = dist[i] + 1
        else:
            dist[i] = 1

    return len(dist)

# print(distinctElements([7,3,2,1,3,7,0]))
