"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.
"""

def topKFrequent(nums,k):
    dist = {}

    for i in range (0, len(nums)):
        if nums[i] in dist: 
            dist[nums[i]] += 1
        else:
            dist[nums[i]] = 1
    
    freq = [0]*len(dist)
    j = 0
    for i in dist:
        freq[j] = [i,dist[i]]
        j += 1
    
    freq.sort(key = lambda x:x[1],reverse=True)

    ans = [0]*k
    for i in range(0,k):
        ans[i] = freq[i][0]

    return ans

print(topKFrequent([1,2,4,5,6,4,3,1,4,9,10],2))
