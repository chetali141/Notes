class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        triangle.append([1])
        for i in range(2,numRows+1):
            row = []
            element = 1
            for j in range(1,i+1):
                row.append(element)
                element = element * (i - j) // j
            triangle.append(row)
        return triangle
