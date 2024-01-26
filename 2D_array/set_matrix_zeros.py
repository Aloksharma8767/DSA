# matrix =[[1,1,1],
#          [1,0,1],
#          [1,1,1]]
matrix=[[0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]]
def setzeros(matrix):
    row, col = len(matrix), len(matrix[0])
    rowzero = False
# Mark the first element of each row and column as 0 if the corresponding row or column has a 0
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowzero = True
# Set the entire row and column to 0 if the first element of the row or column is 0
    for r in range(1, row):
        for c in range(1, col):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
# Set the first column to 0 if the first element of the first column is 0
    if matrix[0][0] == 0:
        for r in range(row):
            matrix[r][0] = 0
# Set the first row to 0 if rowzero is True
    if rowzero:
        for c in range(col):
            matrix[0][c] = 0
setzeros(matrix)
print(matrix)





#leetcode solution
class Solution:
    def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (matrix[row][col] == 0):
                    rows.add(row)
                    cols.add(col)
        for row in rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
        return
        