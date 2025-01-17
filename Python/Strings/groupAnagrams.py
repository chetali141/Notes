"""
Given an array of strings, group all anagrams together into a sublist.
"""

from collections import defaultdict

def groupAnagrams(strs):
    group = defaultdict(list)
    for str in strs:
        count = [0] * 26
        for char in str:
            count[ord(char)-ord('a')] += 1
        group[tuple(count)].append(str)
    return list(group.values())
        

print(groupAnagrams(["abc","def","cba","xyz","mno","nop"]))
