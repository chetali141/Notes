# Reverse the given array - inplace

def reverse(arr):
    start = 0
    end = len(arr) - 1
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1
    return arr

def reversePortion(arr, start, end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1
    return arr

# print(reverse([1,2,3,4,5,6]))
# print(reverse([21,44,56,35,91]))

# print(reversePortion([21,44,65,78,93,15,67], 1, 4))
