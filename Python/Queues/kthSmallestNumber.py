"""
Return kth smallest number that only has digit 2,3.

Approach:

2, 3

2 -> 22, 23
3-> 32, 33

22-> 222,223
23-> 232, 233

and so on ... the numbers having only 2,3 digits can be generated

put 2,3 in queue then take 2 out generate 22,23 and put them in queue and so on until k th times.

Time complexity would be O(k)

"""