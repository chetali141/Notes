"""
given N elements in an array
calculate distinct number of elements in window of length 'k'

total number of windows will be n-k+1
"""

def distinctElementWindow(nums, k):
    number = []
    dist = {}

    for i in range(0, k):
        if nums[i] in dist:
            dist[nums[i]] += 1
        else:
            dist[nums[i]] = 1
    number.append(len(dist))
    
    for i in range(k, len(nums)):
        dist[nums[i-k]] -= 1
        if dist[nums[i-k]] == 0:
            del dist[nums[i-k]]
        if nums[i] in dist:
            dist[nums[i]] += 1
        else:
            dist[nums[i]] = 1
        number.append(len(dist))

    return number

# print(distinctElementWindow([1,1,4,4],2))
# print(distinctElementWindow([6,3,7,3,8,6,9],3))
