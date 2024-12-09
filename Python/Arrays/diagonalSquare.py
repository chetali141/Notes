# Print all diagonals of a square matrix

def printDiagonals(nums):
    # left to right diagonal
    for i in range (0, len(nums)):
        print(nums[i][i])
    
    #right to left diagonal
    for i in range (0, len(nums)):
        print(nums[i][len(nums)-i-1])

# printDiagonals([[1,2,3],[4,5,6],[7,8,9]])
    